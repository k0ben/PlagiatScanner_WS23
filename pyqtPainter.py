from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRectF
import sys
import colorsys

class RainbowWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rainbow In Python PyQt5')
        self.setStyleSheet("background-color: transparent;")
        self.setGeometry(100, 100, 400, 400)
        self.num_colors = 49
        self.radius = 300
        self.penwidth = 20 * 7 / self.num_colors
        self.hue = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the rainbow arcs
        for i in range(self.num_colors):
            (r, g, b) = colorsys.hsv_to_rgb(self.hue, 1, 1)
            color = QColor(int(r * 255), int(g * 255), int(b * 255))
            pen = QPen(color, self.penwidth)
            painter.setPen(pen)
            rect = QRectF(1, 100, 2 * self.radius, 2 * self.radius)
            startAngle = 0 * 16
            arcLength = 180 * 16
            painter.drawArc(rect, startAngle, arcLength)
            self.radius -= (self.penwidth - 1)
            self.hue += 0.9 / self.num_colors

        # Draw the letter P
        painter.setPen(QPen(Qt.darkBlue, 20))
        painter.drawLine(50, 50, 50, 150)  # Vertical line
        painter.drawLine(50, 50, 100, 50)  # Top horizontal line
        painter.drawLine(100, 50, 100, 100)  # Right vertical line
        painter.drawLine(100, 100, 50, 100)  # Bottom horizontal line

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RainbowWidget()
    window.show()
    sys.exit(app.exec_())
