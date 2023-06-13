from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox, QPushButton
from PyQt5.QtCore import Qt, QEvent, QPoint
from arrowbutton_class import LeftArrowLabel
from lang_list_support import languages_list
class SecondScreen(QWidget):
    def __init__(self, parent=None,callback=None, storage=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.callback=callback
        self.parent=parent
        label = QLabel("Settings", self)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.storage2=storage

        self.language_combo = QComboBox(self)
        for language in languages_list:
            self.language_combo.addItem(language)
        self.language_combo.model().sort(0, Qt.AscendingOrder)
        self.language_combo.setCurrentText("English")
        layout.addWidget(self.language_combo)

        self.list_of_files = QComboBox(self)
        self.list_of_files.addItem('None')
        layout.addWidget(self.list_of_files)

        self.file_options= QComboBox(self)
        self.file_options.addItem('Append')
        self.file_options.addItem('Write')
        layout.addWidget(self.file_options)

        self.delete_button = QPushButton("Delete", self)
        layout.addWidget(self.delete_button)
        self.delete_button.clicked.connect(lambda: self.delete_file(self.list_of_files.currentText()))

        self.reset_all_button = QPushButton("Reset all", self)
        layout.addWidget(self.reset_all_button)
        self.reset_all_button.clicked.connect(lambda: self.reset_all())
        
        self.back_to_main_screen_button = QPushButton("Back to Main Screen", self)
        layout.addWidget(self.back_to_main_screen_button)
        self.back_to_main_screen_button.clicked.connect(self.switch_to_previous_screen)

        #self.arrow_label = LeftArrowLabel(self, self.switch_to_previous_screen)
        #layout.addWidget(self.arrow_label)
        self.setLayout(layout)

    def switch_to_previous_screen(self):
        self.callback()
       # print(self.language_combo.currentText())
    def delete_file(self, file):
       # print(self.storage2.list_of_files)
    # Remove file from self.storage2.list_of_files
        if file != 'None':
                # Remove the first occurrence
            removed = False
            # Iterate over the list
            for t in self.storage2.list_of_files:
                if t[1] == file and not removed:
                    self.storage2.list_of_files.remove(t)
                    removed = True
            index = self.list_of_files.findText(file)
            if index != -1:
                self.list_of_files.removeItem(index)
        #print(self.storage2.list_of_files)

    def reset_all(self):
        self.storage2.list_of_files=[]
        self.list_of_files.clear()
        self.list_of_files.addItem('None')



    