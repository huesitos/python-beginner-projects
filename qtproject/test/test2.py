import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel,
                             QHBoxLayout, QVBoxLayout, QPushButton)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel("Hi there, I'm a label.")
        ok_button = QPushButton("OK")
        cancel_button = QPushButton("CANCEL")

        horizontal = QHBoxLayout()
        horizontal.addStretch()

        horizontal.addWidget(ok_button)
        horizontal.addWidget(cancel_button)

        vertical = QVBoxLayout()
        vertical.addWidget(label)
        vertical.addStretch()
        vertical.addLayout(horizontal)

        self.setLayout(vertical)

        self.setWindowTitle("Horizontal Layout")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
