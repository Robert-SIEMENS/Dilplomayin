import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class Discriminator(keras.Model):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.model = self.build_discriminator()

    def build_discriminator(self):
        inputs = layers.Input(shape=(256, 256, 2))  # Input: (Layout, Mask)
        x = layers.Conv2D(64, (4, 4), strides=2, padding="same", activation="relu")(inputs)
        x = layers.Conv2D(128, (4, 4), strides=2, padding="same", activation="relu")(x)
        x = layers.Conv2D(256, (4, 4), strides=2, padding="same", activation="relu")(x)
        x = layers.Conv2D(1, (4, 4), padding="same", activation="sigmoid")(x)
        return keras.Model(inputs, x, name="discriminator")

    def call(self, inputs):
        return self.model(inputs)
