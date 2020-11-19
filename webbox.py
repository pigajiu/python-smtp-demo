# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webbox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import *
class WebBox(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.broswer=QWebEngineView()
        self.broswer.setUrl(QUrl('http://www.baidu.com'))
        self.broswer.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

