import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent, QPainter, QColor, QPolygon

class RightArrowLabel(QLabel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.hovered = False
        self.callback = callback

    def enterEvent(self, event: QEvent):
        self.hovered = True
        self.update()

    def leaveEvent(self, event: QEvent):
        self.hovered = False
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        self.callback()


    def paintEvent(self, event):
        if self.hovered:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            size = self.size()
            width, height = size.width(), size.height()
            arrow_size = min(width, height) - 50

            # Create a QPolygon from the points
            points = QPolygon([
                QPoint(int(width - arrow_size - 10), int(height / 2 - 5)),
                QPoint(int(width - 10), int(height / 2 - 5)),
                QPoint(int(width - 10), int(height / 2 - 15)),
                QPoint(int(width), int(height / 2)),
                QPoint(int(width - 10), int(height / 2 + 15)),
                QPoint(int(width - 10), int(height / 2 + 5)),
                QPoint(int(width - arrow_size - 10), int(height / 2 + 5)),
            ])



            # Draw arrow
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, 100))
            painter.drawPolygon(points)

        super().paintEvent(event)

class LeftArrowLabel(QLabel):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.hovered = False
        self.callback = callback

    def enterEvent(self, event):
        self.hovered = True
        self.update()

    def leaveEvent(self, event):
        self.hovered = False
        self.update()

    def mousePressEvent(self, event):
        self.callback()

    def paintEvent(self, event):
        if self.hovered:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            size = self.size()
            width, height = size.width(), size.height()
            arrow_size = min(width, height) - 50
            arrow_size = min(arrow_size, 30)  # Adjust the arrow size (maximum 30)

            points = QPolygon([
                QPoint(int(arrow_size + 5), int(height / 2 - 3)),
                QPoint(int(5), int(height / 2 - 3)),
                QPoint(int(5), int(height / 2 - 8)),
                QPoint(int(0), int(height / 2)),
                QPoint(int(5), int(height / 2 + 8)),
                QPoint(int(5), int(height / 2 + 3)),
                QPoint(int(arrow_size + 5), int(height / 2 + 3)),
            ])

            painter.translate(width, height)
            painter.rotate(180)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(0, 0, 0, 100))
            painter.drawPolygon(points)

        super().paintEvent(event)




 