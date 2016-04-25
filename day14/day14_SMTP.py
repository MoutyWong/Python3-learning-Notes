#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Python 对SMTP支持有smtplib 和 email两个模块,email 负责构造邮件,smtplib负责发送邮件
# 
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib


# 输入Email地址和口令
from_addr = input('From:')
password = input('Password:')
# 输入收件人地址
to_addr = input('To:')
# 输入SMTP服务器地址
# smtp_server = input('SMTP server:')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

server = smtplib.SMTP('smtp@gmail.com', 587) #SMTP协议默认端口是25
server.starttls()
server.set_debuglevel(1)
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息
server.login(from_addr, password)
# login()方法用来登录SMTP服务器
server.sendmail(from_addr, [to_addr], msg.as_string())
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.quit()
