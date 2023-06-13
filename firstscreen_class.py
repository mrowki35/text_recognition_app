import sys
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QMainWindow, QGridLayout
from PyQt5.QtCore import Qt, QEvent, QPoint, QTimer
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QMouseEvent, QPixmap, QIcon, QFont, QColor
from filebase_class import FilesBase
from text_recognition_function import Text_recognition_handling
from arrowbutton_class import RightArrowLabel
from language_dict import language_dictionary
from support_dictionary import file_options_dictionary
import os

class FileDropWindow(QWidget):
    def __init__(self, parent=None,callback=None,second_page=None, storage=None):
        super().__init__(parent)
        #storage = FilesBase()
        self.callback=callback
        self.second_page = second_page
        self.storage1=storage
        layout = QGridLayout(self)
        layout.setSpacing(10)
        self.setAcceptDrops(True)

        self.label = QLabel("Drop your files here", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.submit_button = QPushButton("Submit", self)
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.submit_action)

        #Displaying if the file is correct
        self.status_label = QLabel(self)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.hide()
        layout.addWidget(self.status_label)

        self.timer = QTimer(self)
        self.timer.setInterval(1500)
        self.timer.timeout.connect(self.hide_status_label)

        self.arrow_label = RightArrowLabel(self, self.switch_to_next_screen)
        layout.addWidget(self.arrow_label)

        self.setLayout(layout)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            file_path = urls[0].toLocalFile()
            # check if the extension is correct
            if self.storage1.check_image_format(file_path):
                self.storage1.list_of_files.append((file_path,os.path.basename(file_path)))
                self.second_page.list_of_files.addItem(os.path.basename(file_path))
                self.show_status_label("File added", QColor("green"))
            else:
                self.show_status_label("Wrong file", QColor("red"))
                
    def switch_to_next_screen(self):
        #print("Switching to the next screen")
        self.callback()

    def submit_action(self):
        #print("Submit button clicked")
        #print("Selected language:", language)
        option = file_options_dictionary[self.second_page.file_options.currentText()]  
        try:
            with open ('where_text_goes.txt',option, encoding='utf-8') as f:
                for path, name in self.storage1.list_of_files:
                    f.write(Text_recognition_handling(path,language_dictionary[self.second_page.language_combo.currentText()]) +'\n')
            f.close()

        except IndexError:
            pass
        except FileNotFoundError:
            pass

    def show_status_label(self, message, color):
        self.status_label.setText(message)
        self.status_label.setStyleSheet(f"background-color: {color.name()}; color: white;")
        self.status_label.show()
        self.timer.start()

    def hide_status_label(self):
        self.status_label.hide()
        self.timer.stop()