import cv2
import keras
import numpy

def testMain():
    model = keras.models.load_model("mnist.keras")
    img = cv2.imread("7.jpg")
    img = cv2.resize(img, (28, 28))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    pixel = []
    for i in range(28):
        for j in range(28):
            pixel.append((255 - gray[i, j]) / 255)
    pixelarray = numpy.asarray([pixel])
    label = model.predict(pixelarray)
    maxindex = numpy.argmax(label)


    print("(number, probability)")
    print(*(f"({x[1]}, {y})\n" for x, y in numpy.ndenumerate(label)))
    if label.max() > 0.8:
        print(maxindex)
    else:
        print("無法確認")
