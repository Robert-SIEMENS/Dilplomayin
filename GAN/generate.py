import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from GAN.generator import Generator  # Ensure Generator class is imported

class MaskGenerator:
    def __init__(self, model_path):
        """Initialize the mask generator by loading the trained model."""
        # self.model = tf.keras.models.load_model(model_path, custom_objects={"Generator": Generator})
        self.model = tf.keras.models.load_model(
            model_path, 
            custom_objects={
                "Generator": Generator, 
                "DTypePolicy": tf.keras.mixed_precision.Policy
            }
        )
        # self.model = tf.keras.models.load_model(model_path, compile=False)
        self.model.compile(optimizer="adam", loss="mse")  # Add appropriate loss function

    
    def generate_mask(self, image_path):
        """Generates a mask for the given image using the trained model."""
        try:
            # Load the image and resize it to match model input
            img = load_img(image_path, target_size=(256, 256), color_mode="grayscale")  # Convert to grayscale
            img = img_to_array(img) / 255.0  # Normalize
            img = np.expand_dims(img, axis=0)  # Add batch dimension


            # Predict mask
            predicted_mask = self.model.predict(img)
            
            # If the model output needs reshaping, adjust accordingly
            predicted_mask = np.squeeze(predicted_mask, axis=0)  # Remove batch dimension
            predicted_mask = np.squeeze(predicted_mask)
            return predicted_mask
        except Exception as e:
            print(f"Error generating mask: {e}")
            return None

    def save_mask(self, mask, save_path="output/generated_mask.png"):
        if isinstance(mask, tuple):  # Ensure it's a NumPy array
            mask = np.array(mask)
        plt.imsave(save_path, mask, cmap="gray")
        print(f"Generated mask saved at {save_path}")


