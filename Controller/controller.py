from PyQt5.QtWidgets import QApplication
import Application
import sys

class Controller:
    def run(self):   
        app = QApplication(sys.argv)
        window = Application.Application.getInstance().getUI()
        window.show()
        sys.exit(app.exec_())