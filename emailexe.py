# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emailexe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
from emailbox import Mailbox

class MyEmailbox(object):
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

    def get_mail_number(self):
        rsp, msg_list, rsp_siz = self.server.list()
        mail_count=msg_list
        return len(mail_count)-1

    def get_one_mail(self,cost):
        msgls = []
        rsp, msg_list, rsp_siz = self.server.list()
        for i in range(cost-1,-1,-1):
            total_mail_numbers = len(msg_list) - i
            rsp, msglines, msgsiz = self.server.retr(total_mail_numbers)
            msg_content = b'\r\n'.join(msglines).decode('utf-8')
            msg = Parser().parsestr(text=msg_content)
            msgls.append(msg)
        return msgls


    def receive_email_info(self):
        rsp, msg_list, rsp_siz = self.server.list()
        msgls=[]
        for i in range (len(msg_list)-1):
            total_mail_numbers=len(msg_list)-i
            rsp, msglines, msgsiz = self.server.retr(total_mail_numbers)
            msg_content = b'\r\n'.join(msglines).decode('utf-8')
            msg = Parser().parsestr(text=msg_content)
            msgls.append(msg)
        return msgls

    def parser_subject(self,msg):
        subject = msg['Subject']
        value, charset = decode_header(subject)[0]
        if charset:
            value = value.decode(charset)
        return value

    def parser_address(self,msg):
        hdr, addr = parseaddr(msg['From'])
        # name 发送人邮箱名称， addr 发送人邮箱地址
        name, charset = decode_header(hdr)[0]
        if charset:
            name = name.decode(charset)
        return addr

    def get_msg_list(self,msg):
        msg = self.receive_email_info()
        self.mail_list = []
        for i in msg:
            sub = self.parser_subject(i)
            addr = self.parser_address(i)
            a = (sub, addr)
            self.mail_list.append(a)
        return self.mail_list


class MyEmail(object):

    def __init__(self,username,password,smtp_server):
        self.username=username
        self.password=password
        self.smtp_server=smtp_server
        self.connect_server()

    def create_email(self,mail_title,receiver):
        message=MIMEMultipart()
        message['From']=self.username
        message['To']=receiver
        message['Subject']=Header(mail_title,'utf-8')
        self.message=message

    def email_appendix(self, file_path):
        att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
        # 指定头部信息
        att1["Content-Type"] = 'application/octet-stream'  # 内容为二进制流
        att1["Content-Disposition"] = 'attachment; filename="%s"' % (os.path.basename(file_path))
        self.message.attach(att1)

    def email_text(self,content,content_type='plain'):
        self.message.attach(MIMEText(content,content_type,'utf-8'))

    def connect_server(self):
        smtpObj=smtplib.SMTP_SSL()
        smtpObj.connect(self.smtp_server)
        try:
            smtpObj.login(self.username,self.password)
        except smtplib.SMTPAuthenticationError:
            print('请检查用户名和授权码是否添加正确！')
            return
        else:
            self.smtpObj=smtpObj

    def send_mail(self,receiver):
        try:
            self.smtpObj.sendmail(self.username, receiver, self.message.as_string())
        except smtplib.SMTPException:
            return 2
        else:
            return 1





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(472, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 10, 341, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 40, 341, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 340, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_3.setObjectName("label_3")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(80, 70, 341, 221))
        self.textEdit_1.setObjectName("textEdit1")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 300, 54, 12))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 300, 211, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setReadOnly(True)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 300, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(310, 340, 111, 41))
        self.toolButton.setObjectName("toolButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.send)
        self.pushButton_2.clicked.connect(MainWindow.openfile)
        self.toolButton.clicked.connect(MainWindow.openbox)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "主题："))
        self.label_2.setText(_translate("MainWindow", "正文："))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.label_3.setText(_translate("MainWindow", "收件人："))
        self.label_4.setText(_translate("MainWindow", "附件："))
        self.pushButton_2.setText(_translate("MainWindow", "选择文件"))
        self.toolButton.setText(_translate("MainWindow", "查看邮件"))

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName(self,'选择文件')
        self.lineEdit_4.setText(openfile_name[0])

    def email_login(self,username,password,smtp_server):
        self.username=username
        self.password=password
        self.smtp_server=smtp_server
        self.obj=MyEmail(username,password,smtp_server)
        self.myemailbox=MyEmailbox(username,password,smtp_server)
        self.msg_list=self.myemailbox.get_msg_list(self.myemailbox.receive_email_info())

    def openbox(self):
        count=self.myemailbox.get_mail_number()
        if(count>len(self.msg_list)):
            self.msg_list=self.myemailbox.get_msg_list(self.myemailbox.get_one_mail(count-len(self.msg_list)))
        self.box=QtWidgets.QWidget()
        self.mailbox=Mailbox(self.username,self.password,self.smtp_server,self.msg_list)
        self.mailbox.setupUi(self.box)
        self.box.show()


    def send(self):
       self.obj.create_email(self.lineEdit_2.text(),self.lineEdit.text())
       if(self.lineEdit_4.text()!=''):
           self.obj.email_appendix(self.lineEdit_4.text())
       self.obj.email_text(self.textEdit_1.toPlainText())
       a = self.obj.send_mail(self.lineEdit.text())
       if(a==1):
           msg_box = QtWidgets.QMessageBox
           msg_box.question(self, '消息', '邮件发送成功！', msg_box.Ok)
       else:
           msg_box = QtWidgets.QMessageBox
           msg_box.question(self, '消息', '邮件发送失败！', msg_box.Ok)


