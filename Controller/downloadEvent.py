from Controller.IEvent import IEvent 
import shutil
from PyQt5.QtWidgets import QFileDialog

class downloadEvent(IEvent):
    def handle(self, ui_instacne):
        save_path, _ = QFileDialog.getSaveFileName(ui_instacne, "Save Result", "", "Images (*.png *.jpg *.bmp)")
        if save_path:
            shutil.copy(ui_instacne.result_image_path, save_path)
            ui_instacne.drop_label.setText(f"Saved at: {save_path}")