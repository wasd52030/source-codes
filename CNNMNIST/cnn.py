from keras import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten


class CNN:
    def __init__(self) -> None:
        self.model = Sequential()

        self.model.add(
            Conv2D(
                filters=16,
                kernel_size=(5, 5),
                padding="same",
                input_shape=(28, 28, 1),
                activation="relu",
            )
        )
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(
            Conv2D(
                filters=36,
                kernel_size=(5, 5),
                padding="same",
                activation="relu",
            )
        )
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Flatten())
        self.model.add(Dense(128, activation="relu"))
        self.model.add(Dense(10, activation="softmax"))

    def summary(self):
        print(self.model.summary())
