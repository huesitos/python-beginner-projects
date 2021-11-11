import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QHBoxLayout, QVBoxLayout, QPushButton)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        self.text_label = QLabel("There has been no name entered, so I can't do anything.")
        self.button = QPushButton("Set Name")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()

        self.button.clicked.connect(self.alter_name)

        hl = QHBoxLayout()
        hl.addWidget(self.label)
        hl.addWidget(self.name_input)

        vl = QVBoxLayout()
        vl.addWidget(self.text_label)
        vl.addLayout(hl)
        vl.addWidget(self.button)

        self.setLayout(vl)

        self.setWindowTitle("Nobody's Window")
        self.show()

    def alter_name(self):
        print("This button has been clicked.")
        input_text = self.name_input.text()
        our_string = "You've entered " + input_text
        self.text_label.setText(our_string)
        self.setWindowTitle(input_text + "'s Window")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
