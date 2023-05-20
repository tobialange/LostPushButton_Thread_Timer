import random
from PyQt6.QtCore import QThread, pyqtSignal, QTimer


class Worker(QThread):

    resultReady = pyqtSignal(int)
    timeReady = pyqtSignal(int)

    def run(self):

        result = random.randint(1, 10)
            #time = result

        self.resultReady.emit(result)

        self.timer = QTimer(self)
        self.timer.start(int(result) * 1000)
        while self.timer.isActive():
            time = self.timer.remainingTime()
            self.timeReady.emit(time)
            #if time < 3000:
             #   crit = "background-color: red"
              #  self.timeCritical.emit(crit)
            #elif time == 0:
             #   alert = "Alarm"
              #  self.alert.emit(alert)
