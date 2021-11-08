import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLineEdit, QTabBar, QShortcut, QSplitter,
                             QFrame, QStackedLayout)
from PyQt5.QtGui import QIcon, QMouseEvent, QKeySequence
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.selectAll()


class Application(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.create_app()
        self.setMinimumSize(1366, 768)
        self.setWindowIcon(QIcon("logo.png"))

    def create_app(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create tab bars
        self.tabbar = QTabBar(movable=True, tabsClosable=True)
        self.tabbar.tabCloseRequested.connect(self.close_tab)
        self.tabbar.tabBarClicked.connect(self.switch_tab)
        self.tabbar.setCurrentIndex(0)
        self.tabbar.setDrawBase(False)
        self.tabbar.setLayoutDirection(Qt.LeftToRight)

        self.shortcut_new_tab = QShortcut(QKeySequence("Ctrl+T"), self)
        self.shortcut_new_tab.activated.connect(self.add_tab)

        self.shortcut_reload = QShortcut(QKeySequence("Ctrl+R"), self)
        self.shortcut_reload.activated.connect(self.reload_page)

        # keep track of tabs
        self.tabCount = 0
        self.tabs = []

        # Create address bar
        self.toolbar = QWidget()
        self.toolbar.setObjectName("Toolbar")
        self.toolbar_layout = QHBoxLayout()
        self.address_bar = AddressBar()
        self.add_tab_button = QPushButton("+")

        self.address_bar.returnPressed.connect(self.browse_to)
        self.add_tab_button.clicked.connect(self.add_tab)

        # Set toolbar buttons
        self.back_button = QPushButton("<")
        self.back_button.clicked.connect(self.go_back)

        self.forward_button = QPushButton(">")
        self.forward_button.clicked.connect(self.go_forward)

        self.reload_button = QPushButton("R")
        self.reload_button.clicked.connect(self.reload_page)

        # Build toolbar
        self.toolbar.setLayout(self.toolbar_layout)
        self.toolbar_layout.addWidget(self.back_button)
        self.toolbar_layout.addWidget(self.forward_button)
        self.toolbar_layout.addWidget(self.reload_button)
        self.toolbar_layout.addWidget(self.address_bar)
        self.toolbar_layout.addWidget(self.add_tab_button)

        # set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)
        self.add_tab()

        self.show()

    def close_tab(self, i):
        self.tabbar.removeTab(i)

    def add_tab(self):
        i = self.tabCount

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].layout.setContentsMargins(0, 0, 0, 0)

        # For tab switching
        self.tabs[i].setObjectName("tab" + str(i))

        # Open webview
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://google.com"))

        self.tabs[i].content.titleChanged.connect(lambda: self.set_tab_content(i, "title"))
        self.tabs[i].content.iconChanged.connect(lambda: self.set_tab_content(i, "icon"))
        self.tabs[i].content.urlChanged.connect(lambda: self.set_tab_content(i, "url"))

        # add webview to tabs layout
        self.tabs[i].split_view = QSplitter()
        # self.tabs[i].split_view.setOrientation(Qt.Vertical)
        self.tabs[i].layout.addWidget(self.tabs[i].split_view)
        self.tabs[i].split_view.addWidget(self.tabs[i].content)

        # set top level tab from [] to layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        # add tab to top level stackedwidget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        # set the tab at top of screen
        self.tabbar.addTab("New Tab")
        self.tabbar.setTabData(i, {"object": "tab"+str(i), "initial": i})
        self.tabbar.setCurrentIndex(i)

        self.tabCount += 1

    def switch_tab(self, i):
        if self.tabbar.tabData(i):
            tab_data = self.tabbar.tabData(i)["object"]
            tab_content = self.findChild(QWidget, tab_data)
            self.container.layout.setCurrentWidget(tab_content)
            # TODO: figure out why this doesn't work
            # new_url = tab_content.url().toString()
            # self.address_bar.setText(new_url)

    def browse_to(self):
        text = self.address_bar.text()
        i = self.tabbar.currentIndex()
        tab = self.tabbar.tabData(i)["object"]
        web_view = self.findChild(QWidget, tab).content

        if "http" not in text:
            if "." not in text:
                url = "https://www.google.com/#q=" + text
            else:
                url = "http://" + text
        else:
            url = text

        web_view.load(QUrl.fromUserInput(url))

    def set_tab_content(self, i, content_type):
        tab_name = self.tabs[i].objectName()
        count = 0
        running = True

        current_tab = self.tabbar.tabData(self.tabbar.currentIndex())["object"]

        if current_tab == tab_name and content_type == "url":
            #new_url = self.findChild(QWidget, tab_name).content.url().toString()
            #self.address_bar.setText(new_url)
            return False

        while running:
            tab_data_name = self.tabbar.tabData(count)

            if count >= 99:
                running = False

            if tab_name == tab_data_name["object"]:
                if content_type == "title":
                    new_title = self.findChild(QWidget, tab_name).content.title()
                    self.tabbar.setTabText(count, new_title)
                elif content_type == "icon":
                    new_icon = self.findChild(QWidget, tab_name).content.icon()
                    self.tabbar.setTabIcon(count, new_icon)

                running = False
            else:
                count += 1

    def go_back(self):
        active_index = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.back()

    def go_forward(self):
        active_index = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.forward()

    def reload_page(self):
        active_index = self.tabbar.currentIndex()
        tab_name = self.tabbar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.reload()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = "667"

    window = Application()

    with open("style.css", "r") as style:
        app.setStyleSheet(style.read())

    sys.exit(app.exec_())
