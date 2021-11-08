import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QHBoxLayout, QVBoxLayout, QPushButton)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.counter = 0

    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked: ")
        self.button.pressed.connect(self.pressed_button)
        self.button.released.connect(self.released_button)

        hl = QHBoxLayout()
        hl.addStretch()
        hl.addWidget(label)
        hl.addWidget(name_input)

        vl = QVBoxLayout()
        vl.addStretch(1)
        vl.addLayout(hl)
        vl.addWidget(self.button)

        self.setLayout(vl)

        self.setWindowTitle("Horizontal Layout")
        self.show()

    def pressed_button(self):
        print("This button has been clicked.")
        self.counter += 1
        self.button.setText("Clicked: " + str(self.counter))

    def released_button(self):
        print("This button has been released.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
