from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from Controller.IEvent import IEvent

class uploadEvent(IEvent):
    def handle(self, ui_instance):
        file_path = ui_instance.image_path 
        if file_path is None:
            file_path, _ = QFileDialog.getOpenFileName(ui_instance, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        
        ui_instance.image_path = file_path
        ui_instance.drop_label.setText(f"Selected: {os.path.basename(file_path)}")
        pixmap = QPixmap(file_path).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        ui_instance.upload_icon.setPixmap(pixmap)
        ui_instance.run_button.setVisible(True)
