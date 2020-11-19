import sys
import smtplib
from emailexe import Ui_MainWindow
from email_login import Ui_Form
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from PyQt5 import  QtWidgets

class Login(Ui_Form,QWidget):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)


    def jump(self):
        qqform = '@qq.com'
        form163 = '@163.com'
        username,password=self.check()
        if(qqform in username):
            smtpObj = smtplib.SMTP_SSL()
            smtpObj.connect('smtp.qq.com')
            try:
                smtpObj.login(username, password)
            except smtplib.SMTPAuthenticationError:
                msg_box = QtWidgets.QMessageBox
                msg_box.question(self, '消息', '请检查用户名和授权码是否添加正确！', msg_box.Ok, msg_box.Cancel)
                return
            else:
                msg_box = QtWidgets.QMessageBox
                msg_box.question(self, '消息', '登录成功！', msg_box.Ok, msg_box.Cancel)
                self.emailwindow = Emailwindow()
                self.emailwindow.show()
                self.emailwindow.email_login(username, password,'smtp.qq.com')
                self.close()
        elif (form163 in username):
            smtpObj = smtplib.SMTP_SSL()
            smtpObj.connect('smtp.163.com')
            try:
                smtpObj.login(username, password)
            except smtplib.SMTPAuthenticationError:
                msg_box = QtWidgets.QMessageBox
                msg_box.question(self, '消息', '请检查用户名和授权码是否添加正确！', msg_box.Ok, msg_box.Cancel)
                return
            else:
                msg_box = QtWidgets.QMessageBox
                msg_box.question(self, '消息', '登录成功！', msg_box.Ok, msg_box.Cancel)
                self.emailwindow = Emailwindow()
                self.emailwindow.email_login(username,password,'smtp.163.com')
                self.emailwindow.show()
                self.close()
        else:
            print('error')



class Emailwindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__=='__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec_())