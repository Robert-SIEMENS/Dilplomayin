import tensorflow as tf
from tensorflow import keras
from GAN.generator import Generator
from GAN.discriminator import Discriminator

class Pix2PixGAN(keras.Model):
    def __init__(self):
        super(Pix2PixGAN, self).__init__()
        self.generator = Generator()
        self.discriminator = Discriminator()
        self.loss_fn = keras.losses.BinaryCrossentropy(from_logits=True)

    def compile(self, gen_optimizer, disc_optimizer):
        super(Pix2PixGAN, self).compile()
        self.gen_optimizer = gen_optimizer
        self.disc_optimizer = disc_optimizer

    def train_step(self, batch):
        layout, mask = batch
        fake_mask = self.generator(layout)

        # Train Discriminator
        with tf.GradientTape() as disc_tape:
            real_output = self.discriminator(tf.concat([layout, mask], axis=-1))
            fake_output = self.discriminator(tf.concat([layout, fake_mask], axis=-1))
            real_loss = self.loss_fn(tf.ones_like(real_output), real_output)
            fake_loss = self.loss_fn(tf.zeros_like(fake_output), fake_output)
            disc_loss = real_loss + fake_loss

        disc_grads = disc_tape.gradient(disc_loss, self.discriminator.trainable_variables)
        self.disc_optimizer.apply_gradients(zip(disc_grads, self.discriminator.trainable_variables))

        # Train Generator
        with tf.GradientTape() as gen_tape:
            fake_mask = self.generator(layout)
            fake_output = self.discriminator(tf.concat([layout, fake_mask], axis=-1))
            gen_loss = self.loss_fn(tf.ones_like(fake_output), fake_output)

        gen_grads = gen_tape.gradient(gen_loss, self.generator.trainable_variables)
        self.gen_optimizer.apply_gradients(zip(gen_grads, self.generator.trainable_variables))

        return {"gen_loss": gen_loss, "disc_loss": disc_loss}
