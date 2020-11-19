import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class webWindow(object):
    def __init__(self,url):
        super(webWindow, self).__init__()
        self.url=''''''+url

    def setupUI(self,Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl(self.url))
        self.setCentralWidget(self.browser)

