import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt, QEvent, QPoint
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent, QPainter, QColor, QPolygon
from filebase_class import FilesBase
from text_recognition_function import Text_recognition_handling
from firstscreen_class import FileDropWindow
from second_screen_class import SecondScreen
from filebase_class import FilesBase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text recognition app")
        self.setGeometry(100, 100, 300, 200)

        storage=FilesBase()

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.second_page = SecondScreen(self,self.switch_to_main_screen, storage)
        self.stacked_widget.addWidget(self.second_page)

        self.first_page = FileDropWindow(self,self.switch_to_second_screen,self.second_page, storage)
        self.stacked_widget.addWidget(self.first_page)

        self.show_first_page()

    def show_first_page(self):
        self.stacked_widget.setCurrentWidget(self.first_page)

    def show_second_page(self):
        self.stacked_widget.setCurrentWidget(self.second_page)


    def switch_to_second_screen(self):
       # print("Switching to the second screen")
        self.show_second_page()

    def switch_to_main_screen(self):
        #print("Switching to the main screen")
        self.show_first_page()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setAcceptDrops(True)
    sys.exit(app.exec_())
    