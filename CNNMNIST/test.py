import tkinter
from PIL import ImageGrab
import cv2
from matplotlib import pyplot
import tensorflow
import numpy

class testApp:
    def __init__(self) -> None:
        self.model = tensorflow.keras.models.load_model("CNNMNIST.keras")
        self.fileName = "test.jpg"

        self.root = tkinter.Tk()

        self.canvas1 = tkinter.Canvas(self.root, width=280, height=280, bg="white")
        self.canvas1.pack()
        self.canvas1.bind("<B1-Motion>", self.paint)


        self.textValue = tkinter.StringVar()
        self.textValue.set("")
        self.label1 = tkinter.Label(textvariable=self.textValue).pack()
        self.button = tkinter.Button(text="辨識", command=self.predict).pack()
        self.button = tkinter.Button(text="清除", command=self.clear).pack()

        self.root.mainloop()


    def paint(self,event):
        x1, y1 = (event.x + 1), (event.y + 1)
        x2, y2 = (event.x - 1), (event.y - 1)
        self.canvas1.create_oval(x1, y1, x2, y2, fill="black", width=15)  # On tkinter Canvas


    def clear(self):
        self.canvas1.delete("all")


    def predict(self):
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        x1 = x + self.canvas1.winfo_width()
        y1 = y + self.canvas1.winfo_height()

        # ref -> https://www.geeksforgeeks.org/python-pil-imagegrab-grab-method/
        canvas=ImageGrab.grab().crop((x, y, x1, y1))# .save(self.fileName)

        img=cv2.cvtColor(numpy.array(canvas),cv2.COLOR_RGB2BGR)
        img = cv2.resize(img, (28, 28))
        pixel = (255 - cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)) / 255  # RGB->GRAY
        fig = pyplot.gcf()
        fig.set_size_inches(2, 2)

        # pyplot.imshow(pixel, cmap="binary")
        # pyplot.show()

        # for Convolutional Neural Network(CNN)
        pixelarray = pixel.reshape(-1, 28, 28, 1)
        
        # for multilayer perceptron(MLP)
        # pixelarray = numpy.asarray([pixel]) 
        # pixelarray = pixelarray.reshape(1, -1)

        label = self.model.predict(pixelarray)
        maxindex = numpy.argmax(label)
        if label.max() > 0.5:
            showtext = f"辨識結果 = {maxindex}, 機率 = {label[0][maxindex]}"
            print(showtext)
            self.textValue.set(showtext)
        else:
            print("無法辨識")

