import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


class Generator(keras.Model):
    def __init__(self, **kwargs):  # Accept extra arguments like 'trainable'
        super(Generator, self).__init__(**kwargs)
        self.encoder = self.build_encoder()
        self.decoder = self.build_decoder()

    def build_encoder(self):
        inputs = layers.Input(shape=(256, 256, 1))
        x = layers.Conv2D(64, (4, 4), strides=2, padding="same", activation="relu")(inputs)
        x = layers.Conv2D(128, (4, 4), strides=2, padding="same", activation="relu")(x)
        x = layers.Conv2D(256, (4, 4), strides=2, padding="same", activation="relu")(x)
        return keras.Model(inputs, x, name="encoder")

    def build_decoder(self):
        inputs = layers.Input(shape=(32, 32, 256))
        x = layers.Conv2DTranspose(128, (4, 4), strides=2, padding="same", activation="relu")(inputs)
        x = layers.Conv2DTranspose(64, (4, 4), strides=2, padding="same", activation="relu")(x)
        x = layers.Conv2DTranspose(1, (4, 4), strides=2, padding="same", activation="tanh")(x)
        return keras.Model(inputs, x, name="decoder")

    def call(self, inputs):
        encoded = self.encoder(inputs)
        decoded = self.decoder(encoded)
        return decoded
