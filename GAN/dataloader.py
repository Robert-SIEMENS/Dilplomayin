import os
import numpy as np
import tensorflow as tf

class DataLoader:
    def __init__(self, layout_path, mask_path):
        self.layout_path = layout_path
        self.mask_path = mask_path
        self.image_size = (256, 256)

    def load_images(self):
        layouts = []
        masks = []
        files = os.listdir(self.layout_path)
        for file in files:
            layout = self.load_image(os.path.join(self.layout_path, file))
            mask = self.load_image(os.path.join(self.mask_path, file.replace(".png", "_res.png")))
            layouts.append(layout)
            masks.append(mask)
        return np.array(layouts), np.array(masks)

    def load_image(self, path):
        img = tf.keras.preprocessing.image.load_img(path, target_size=self.image_size, color_mode="grayscale")
        img = tf.keras.preprocessing.image.img_to_array(img) / 255.0  # Normalize
        return img
