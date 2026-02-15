import os
from Controller.IEvent import IEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from GAN.train import train
from GAN.generate import MaskGenerator

class runEvent(IEvent):
    def handle(self, ui_instance):
        if ui_instance.image_path:
            ui_instance.drop_label.setText("Processing Image...")

            model_path = "C:/dev/Diplom/generator_model.h5"

            if not os.path.exists(model_path):
                ui_instance.drop_label.setText("Training model... Please wait.")
                train(epochs=50, batch_size=16)  # Train and save the generator

            # Use the trained generator to create a mask
            generator = MaskGenerator(model_path)
            result_path = "C:/dev/Diplom/result.png"
            mask = generator.generate_mask(ui_instance.image_path)
            generator.save_mask(mask, result_path)

            # Update UI with the result image
            ui_instance.drop_label.setText("Processing Complete!")
            ui_instance.result_image_path = result_path
            pixmap = QPixmap(result_path)
            ui_instance.upload_icon.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            ui_instance.download_button.setVisible(True)

            # Reset selected image path
            ui_instance.image_path = None
