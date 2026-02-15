import tensorflow as tf
from GAN.gan import Pix2PixGAN
from GAN.dataloader import DataLoader
from tensorflow.keras.callbacks import ModelCheckpoint

def train(epochs=50, batch_size=16):
    data_loader = DataLoader("G:/Hripsime/Education/UNI/4rd_kurs/Diploma project/Code/Diploma-Project/Train data/train_layouts", 
                             "G:/Hripsime/Education/UNI/4rd_kurs/Diploma project/Code/Diploma-Project/Train data/train_masks/")
    layouts, masks = data_loader.load_images()
    dataset = tf.data.Dataset.from_tensor_slices((layouts, masks)).batch(batch_size)
    gan = Pix2PixGAN()
    gan.compile(gen_optimizer=tf.keras.optimizers.Adam(2e-4, beta_1=0.5),
                disc_optimizer=tf.keras.optimizers.Adam(2e-4, beta_1=0.5))

    # Save the generator model after each epoch
    checkpoint_callback = ModelCheckpoint("generator_epoch_{epoch:02d}.h5", save_best_only=False, save_freq='epoch')

    gan.fit(dataset, epochs=epochs, callbacks=[checkpoint_callback])

    # Save the final models
    gan.generator.save("generator_model.h5")
    gan.discriminator.save("discriminator_model.h5")
    print("Models saved successfully!")

if __name__ == "__main__":
    train()
