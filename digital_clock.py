import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel
from PyQt5.QtCore import Qt,QTimer,QTime


class digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)

        self.initUi()

    def initUi(self):
        self.clock_label = QLabel(self)
        self.setWindowTitle("digital clock")
        vbox = QVBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.clock_label)

        self.setGeometry(700,300,500,100)
        self.clock_label.setAlignment(Qt.AlignCenter)

        self.clock_label.setStyleSheet("font-size:100px;" "color:green;")
        self.setStyleSheet("background-color:black;")

        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

        self.update()

    def update(self):
        current_time = QTime.currentTime().toString('hh:mm:ss AP')
        self.clock_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = digital_clock()
    clock.show()
    sys.exit(app.exec_())