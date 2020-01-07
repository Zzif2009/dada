from PIL import Image, ImageDraw
import sys, random
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLineEdit, QInputDialog, QColorDialog
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen, QPolygon, QImage, QPalette
from PyQt5.QtCore import Qt, QPoint


class Paint(QWidget):
    def __init__(self):
        super().__init__()
        self.f, self.x, self.y = 0, 0, 0
        self.setMouseTracking(True)
        uic.loadUi("UI.ui", self)
        self.clicked = False
        self.initUI()

    def initUI(self):
        self.button.clicked.connect(self.click)
        self.show()

    def click(self):
        new_cvet = (255, 255, 255)
        new_image = Image.new("RGB", (500, 500), new_cvet)
        image = ImageDraw.Draw(new_image)
        x = random.choice(range(10, 300))
        y = random.choice(range(10, 300))
        d = random.choice(range(10, 200))
        image.ellipse((x, y, x + d, y + d), fill=(255, 255, 0))
        new_image.save("background.jpg")

        back_image = QImage("background.jpg")
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(back_image))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fl = Paint()
    sys.exit(app.exec())
