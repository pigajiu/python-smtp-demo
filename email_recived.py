import poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

class AcceptEmail(object):
    def __init__(self,user_email,password,pop3_server='pop.qq.com'):
        self.usermail=user_email
        self.password=password
        self.pop3_server=pop3_server
        self.connect_email_server()

    def connect_email_server(self):
        self.server=poplib.POP3(self.pop3_server)
        print('连接成功 -- ', self.server.getwelcome().decode('utf8'))
        self.server.user(self.usermail)
        self.server.pass_(self.password)

    def __del__(self):
        # 关闭与服务器的连接，释放资源
        self.server.close()
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
        # return msgls
        # rsp, msglines, msgsiz = self.server.retr(total_mail_numbers)
        # print("服务器的响应: {0},\n原始邮件内容： {1},\n该封邮件所占字节大小： {2}".format(rsp, msglines, msgsiz))
        # msg_content = b'\r\n'.join(msglines).decode('gbk')
        # msg = Parser().parsestr(text=msg_content)
        # print('解码后的邮件信息:\n{}'.format(msg))

    def parser_subject(self,msg):
        subject = msg['Subject']
        value, charset = decode_header(subject)[0]
        if charset:
            value = value.decode(charset)
        return value
        # print(value)
        # print('邮件主题： {0}'.format(value))

    from email.utils import parseaddr

    def parser_address(self,msg):
        hdr, addr = parseaddr(msg['From'])
        # name 发送人邮箱名称， addr 发送人邮箱地址
        name, charset = decode_header(hdr)[0]
        if charset:
            name = name.decode(charset)
        return addr
        # print(addr)
        # print('发送人邮箱名称: {0}，发送人邮箱地址: {1}'.format(name, addr))


if __name__ == '__main__':
    obj=AcceptEmail('630907423@qq.com','ezhndoswuuihbece')
    msg=obj.receive_email_info()
    mail_list=[]
    for i in msg:
        sub=obj.parser_subject(i)
        addr=obj.parser_address(i)
        a=(sub,addr)
        mail_list.append(a)
    print(mail_list)
    print(len(mail_list))
