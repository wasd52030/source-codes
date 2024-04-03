from keras.datasets import mnist
from matplotlib import pyplot
from keras.utils.np_utils import to_categorical
from cnn import CNN

def preprocess(data):
    (x_train, y_train), (x_test, y_test) = data

    # reshape to 4d tensor
    xTrain = x_train.reshape(-1, 28, 28, 1).astype("float32")
    xTest = x_test.reshape(-1, 28, 28, 1).astype("float32")

    # normalize
    xTrain /= 255
    xTest /= 255

    # one-hot encoding
    yTrain = to_categorical(y_train, num_classes=10)
    yTest = to_categorical(y_test, num_classes=10)

    return ((xTrain, yTrain), (xTest, yTest))


# show train history
def showTrainHistory(train_history):
    pyplot.plot(train_history.history["accuracy"])
    pyplot.plot(train_history.history["val_accuracy"])
    pyplot.title("Train History")
    pyplot.ylabel("accuracy")
    pyplot.xlabel("Epoch")
    pyplot.legend(["train", "validation"], loc="upper left")
    pyplot.show()


def trainMain():
    (x_train, y_train), (x_test, y_test) = preprocess(mnist.load_data())

    # compile model
    cnn = CNN()
    cnn.summary()
    cnn.model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )

    # train
    train_history = cnn.model.fit(
        x_train, y_train, validation_split=0.2, batch_size=200, epochs=20, verbose=1
    )
    showTrainHistory(train_history)

    # evaluate model
    loss, accuracy = cnn.model.evaluate(x_test, y_test)
    print("test loss: ", loss)
    print("test accuracy: ", accuracy)

    # save moel file
    cnn.model.save("CNNMNIST.keras")
