from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QProgressBar
from PyQt6.QtCore import pyqtSlot
from Worker import Worker


class MyWidget(QWidget):
    handelResult = pyqtSlot(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.dumm = 0

        self.worker = Worker(100*1000, self)
        self.worker.resultReady.connect(self.handelResult)
        #self.worker.finished.connect(self.worker.deleteLater) #Speicher wird wieder frei sobald Thread fertig ist! Dann muss der Thread aber neu gestartet werden!

        myLayout = QGridLayout(self)
        self.setLayout(myLayout)

        self.startButton = QPushButton("Start", self)
        self.startButton.clicked.connect(self.handelStart)

        self.stopButton = QPushButton("Stop", self)
        self.stopButton.clicked.connect(self.handelStop)

        self.pauseButton = QPushButton("Pause", self)
        self.pauseButton.clicked.connect(self.handelPause)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setText("Ready")

        self.progressBar = QProgressBar(self)
        self.worker.progress.connect(self.progressBar.setValue)

        myLayout.addWidget(self.startButton, 1, 1)
        myLayout.addWidget(self.pauseButton, 1, 2)
        myLayout.addWidget(self.stopButton, 1, 3)
        myLayout.addWidget(self.lineEdit, 2, 1, 1, 2)
        myLayout.addWidget(self.progressBar, 3, 1, 1, 2)

    def handelResult(self, result):
        self.lineEdit.setText(result)

    def handelStart(self):
        self.worker.start()
        self.lineEdit.setText("Thread started")

    def handelStop(self):
        self.worker.terminate()
        self.worker.wait()
        self.dumm = 0

        #self = brauche es überall nicht nur in der einen Funktion!

    def handelPause(self):
        self.progress = self.progressBar.value()
        self.worker.terminate()
        self.worker.wait()
        self.dumm = 1
