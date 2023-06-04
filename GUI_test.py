import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from filebase_class import FilesBase
from PyQt5.QtGui import QDragEnterEvent, QDropEvent
#from main import Text_recognition_handling

class FileDropWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.storage = FilesBase()
        self.setWindowTitle("Text recognition app")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.label = QLabel("Drop your files here", self)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.submit_button = QPushButton("Submit", self)
        layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.submit_action)

        central_widget.setLayout(layout)
        self.show()

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            file_path = urls[0].toLocalFile()
            self.storage.list_of_files.append(file_path)
            print("File dropped:", file_path)

    def submit_action(self):
        print("Submit button clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FileDropWindow()
    sys.exit(app.exec_())
