import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MyEmail(object):

    def __init__(self,sender,receiver,username,password,smtp_server='smtp.qq.com'):
        self.sender=sender
        self.receiver=receiver
        self.username=username
        self.password=password
        self.smtp_server=smtp_server

        self.connect_server()

    def create_email(self,mail_title):
        message=MIMEMultipart()
        message['From']=self.sender
        message['To']=self.receiver
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

    def send_mail(self):
        self.smtpObj.sendmail(self.sender,self.receiver,self.message.as_string())
        print("邮件发送成功！！！")

    def __del__(self):
        self.smtpObj.close()

if __name__=='__main__':
    obj=MyEmail(sender='630907423@qq.com',receiver='2272538773@qq.com',username='630907423@qq.com',password='ezhndoswuuihbece')
    obj.create_email('megumi kato')
    # obj.email_appendix('D:/pycharm_project/email/remu.jpg')
    obj.email_text('hello dbsmouse')
    obj.send_mail()