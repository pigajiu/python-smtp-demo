# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emailbox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from email.parser import Parser
import poplib
from PyQt5 import QtCore, QtGui, QtWidgets
from webbox2 import WebBox2

class OneMail(object):
    def __init__(self,username,password,smtp_server):
        self.username=username
        self.password=password
        self.smtp_server=smtp_server
        self.connect_server()

    def connect_server(self):
        if('qq'in self.smtp_server):
            self.server = poplib.POP3('pop.qq.com')
        else:
            self.server = poplib.POP3('pop.163.com')
        self.server.user(self.username)
        self.server.pass_(self.password)

    def print_info(self,msg, indent=0):
        if (msg.is_multipart()):
            parts = msg.get_payload()
            for n, part in enumerate(parts):
                # print('%spart %s' % ('  ' * indent, n))
                # print('%s--------------------' % ('  ' * indent))
                self.print_info(part, indent + 1)
        else:
            content_type = msg.get_content_type()
            if content_type == 'text/plain' or content_type == 'text/html':
                content = msg.get_payload(decode=True)
                charset = self.guess_charset(msg)
                if charset:
                    content = content.decode(charset)
                    self.allcontent+=content
                # print('%sText: %s' % ('  ' * indent, content + '...'))
            else:
                print('%sAttachment: %s' % ('  ' * indent, content_type))

    def guess_charset(self,msg):
        charset = msg.get_charset()
        if charset is None:
            content_type = msg.get('Content-Type', '').lower()
            pos = content_type.find('charset=')
            if pos >= 0:
                charset = content_type[pos + 8:].strip()
        return charset

    def get_one_mail(self,index):
        self.allcontent=''''''
        resp, lines, octets = self.server.retr(index)
        msg_content = b'\r\n'.join(lines).decode('utf-8')
        msg = Parser().parsestr(msg_content)
        self.print_info(msg)
        return self.allcontent


class MailBrowser2(QtWidgets.QMainWindow,WebBox2):
    def __init__(self,html):
        super(MailBrowser2, self).__init__()
        self.setupUi(self)
        self.broswer.setHtml(html)
        self.setCentralWidget(self.broswer)


class Mailbox(object):
    def __init__(self,username,password,smtp_server,msg_list):
        super(Mailbox,self).__init__()
        self.username=username
        self.password=password
        self.smtp_server=smtp_server
        self.msg_list = msg_list
        self.onemail=OneMail(self.username,self.password,self.smtp_server)


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 290)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 451, 271))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.msg_list))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        for i in range(len(self.msg_list)):
            for q in range(2):
                newItem = QtWidgets.QTableWidgetItem(self.msg_list[i][q])
                self.tableWidget.setItem(i,q,newItem)
        self.tableWidget.doubleClicked.connect(self.table_change)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "标题"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "发件人"))


    def table_change(self, index):
        row = index.row()
        content=self.onemail.get_one_mail(len(self.msg_list)-row+1)
        # print(content)
        # self.box = QtWidgets.QDialog
        self.webbox = MailBrowser2(content)
        # self.webbox.setupUi(self.box)
        self.webbox.show()
        #


