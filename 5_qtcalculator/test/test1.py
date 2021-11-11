#!/usr/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Page(QWidget):
    def __init__(self, parent=None):
        super(Page, self).__init__(parent)
        my_label = QLabel("This is my label")
        layout = QVBoxLayout()

        layout.addWidget(my_label)

        main_layout = QGridLayout()
        main_layout.addLayout(layout, 0, 1)

        self.setLayout(main_layout)
        self.setWindowTitle("My First Qt App")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec_())
