from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor

from PyQt5 import uic
from random import randint


class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('test1.ui', self)
        self.setGeometry(500, 500, 500, 500)
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        tru = QPixmap(500, 500)
        self.label.setPixmap(tru)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 10, 0)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x = randint(10, 400)
        y = randint(10, 400)
        h1 = randint(10, 100)
        h2 = h1

        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(229, 235, 52))
        painter.setPen(pen)
        painter.drawEllipse(x, y, h1, h2)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Test()
    w.show()
    sys.exit(app.exec_())
