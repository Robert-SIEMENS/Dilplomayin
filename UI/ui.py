from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from Controller.runEvent import runEvent
from Controller.uploadEvent import uploadEvent
from Controller.downloadEvent import downloadEvent

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.image_path = None
        self.result_image_path = None
        self.init_ui()

        self.event_map = {
            "upload": uploadEvent(),
            "run": runEvent(),
            "download": downloadEvent(),
        }


    def init_ui(self):
        self.setWindowTitle("Mask Optimization Algorithm")
        self.setGeometry(100, 100, 500, 450)
        self.setStyleSheet("background-color: #ADD8E6;")

        layout = QVBoxLayout(self)

        title_label = QLabel("Upload Layout", self)
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #003399;")
        layout.addWidget(title_label)

        self.drop_area = QFrame(self)
        self.drop_area.setStyleSheet(
            "background-color: #f7faff; border-radius: 12px; border: 2px dashed #a0c4ff; padding: 40px;")
        self.drop_area.setFrameShape(QFrame.StyledPanel)
        layout.addWidget(self.drop_area)

        drop_layout = QVBoxLayout(self.drop_area)

        self.upload_icon = QLabel(self.drop_area)
        self.upload_icon.setPixmap(QPixmap("C:/dev/Diplom/UI/upload_icon.png").scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.upload_icon.setAlignment(Qt.AlignCenter)
        drop_layout.addWidget(self.upload_icon)

        self.drop_label = QLabel("Drag & drop your layout image here", self.drop_area)
        self.drop_label.setFont(QFont("Arial", 10))
        self.drop_label.setAlignment(Qt.AlignCenter)
        drop_layout.addWidget(self.drop_label)

        self.attach_button = self.create_button("Choose Image", "#003399", lambda: self.sendEvent("upload"))
        layout.addWidget(self.attach_button)

        self.run_button = self.create_button("Run", "#003399", lambda: self.sendEvent("run"), visible=False)
        layout.addWidget(self.run_button)

        self.download_button = self.create_button("Download Result", "#28a745", lambda: self.sendEvent("download"), visible=False)
        layout.addWidget(self.download_button)

        self.setAcceptDrops(True)

    def create_button(self, text, color, callback, visible=True):
        button = QPushButton(text, self)
        button.setStyleSheet(
            f"background-color: white; border: 2px solid {color}; color: {color}; "
            "padding: 10px; border-radius: 8px;")
        button.clicked.connect(callback)
        button.setVisible(visible)
        return button


    def sendEvent(self, event_type):
        event = self.event_map.get(event_type)
        if event:
            event.handle(self)
        else:
            print(f"Unknown event type: {event_type}")


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if file_path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp")):
                self.image_path = file_path
                self.sendEvent("upload")
            else:
                self.drop_label.setText("Invalid file type! Please drop an image.")