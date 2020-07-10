# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

def send_mail(email_user, email_pwd, recv, title, content, mail_host='smtp.163.com', port=25):
    '''
    发送邮件函数

    username: 邮箱账号，发送者账号 xx@163.com
    passwd: 邮箱授权码(不是邮箱的登录密码，是邮箱授权码,参考：https://jingyan.baidu.com/article/c275f6ba33a95de33d7567d9.html)
    recv: 邮箱接收人地址，多个账号以逗号隔开
    title: 邮件标题
    content: 邮件内容
    mail_host: 邮箱服务器，163邮箱host: smtp.163.com
    port: 邮箱端口号,163邮箱的默认端口是 25
        
    测试：
    $ python send_mail.py 
    python3.7.5 测试通过
    '''

    msg = MIMEText(content)  # 邮件内容
    msg['Subject'] = title   # 邮件主题
    msg['From'] = email_user   # 发送者账号
    msg['To'] = recv      # 接收者账号列表
    smtp = smtplib.SMTP(mail_host, port=port)   # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
    smtp.login(email_user, email_pwd)          # 登录发送者的邮箱账号，密码
    # 参数分别是 发送者，接收者，第三个是把上面的发送邮件的 内容变成字符串
    smtp.sendmail(email_user, recv, msg.as_string())
    smtp.quit() # 发送完毕后退出smtp
    

if __name__ == '__main__':
    import time
    email_user = 'wcl6005@163.com' # 发送者账号
    email_pwd = 'wcl6005' # 发送者授权码
    maillist = 'wcl6005@126.com' # 邮箱接收人地址
    title = '邮件标题'
    content = '邮件内容: 从%s发来的邮件。%s'%(email_user, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    send_mail(email_user, email_pwd, maillist, title, content)
    print('OK! Email send success.')
