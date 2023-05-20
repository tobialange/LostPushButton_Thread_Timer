from PyQt6.QtWidgets import QMainWindow
from LostPushButton import LostPushButton


class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(LostPushButton(self))
