from PyQt6.QtWidgets import QGridLayout, QPushButton, QMessageBox
from PyQt6.QtCore import pyqtSlot
from Worker import Worker


class LostPushButton(QPushButton):
    handelResult = pyqtSlot(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.worker = Worker(self)
        self.worker.resultReady.connect(self.handelResult)
        self.worker.timeReady.connect(self.handletime)
        #self.worker.finished.connect(self.worker.deleteLater)

        myLayout = QGridLayout(self)
        self.setLayout(myLayout)

        self.LostButton = QPushButton("LostButton", self)
        self.LostButton.clicked.connect(self.handelStart)

        self.messagebox = QMessageBox()
        myLayout.addWidget(self.LostButton, 1, 1)
        self.noalert = True

    def handelResult(self, result):
        self.LostButton.setText(str(result))
        #self.timer(result)

    def handelStart(self):
        self.noalert = True
        self.worker.terminate()
        self.worker.wait()
        self.worker.start()
        print("gestartet")

    def handletime(self,time):
        self.LostButton.setText(str(time))

        if time >3001:
            self.LostButton.setStyleSheet("background-color: white")

        elif self.noalert and time < 3000:
            self.alarm(time)


    def alarm(self,time):


        self.LostButton.setStyleSheet("background-color: red")

        if time == 0:
            self.messagebox.setText("Alarm")
            self.messagebox.show()
            self.noalert = False