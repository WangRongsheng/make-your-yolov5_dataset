# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart      # 一封邮件
import time

'''
126邮箱IMAP/SMTP服务
授权码：RHNLWUVVNXNYCEFX
'''
    
def sendMail(subject='程序完成情况',msg='您的程序已经运行完成，请去AI Studio查看日志结果',to_list=['603329354@qq.com']):
    sender = 'nicewangrs@126.com'
    sender_password='RHNLWUVVNXNYCEFX'
 

    # 创建邮箱
    em = MIMEMultipart()
    em['subject'] = subject
    em['From'] = sender
    em['To'] = ",".join(to_list)

    # 邮件的内容
    content = MIMEText(msg)
    em.attach(content)

    # 发送邮件
    # 1、连接服务器
    # print("开始连接服务器")
    #25端口已经被云服务器商关闭了，所以只能用465端口了
    smtp=smtplib.SMTP_SSL('smtp.126.com',465)

    # print("连接服务器成功")
    # 2、登录
    # print("开始登录服务器")
    smtp.login(sender, sender_password)
    # print("登录服务器成功")
    # 3、发邮件
    # print("开始发送邮件")
    smtp.send_message(em)
    # print("发送邮件成功")
    # 4、关闭连接
    smtp.close()
#把'2839953196@qq.com' 改为自己的邮箱即可
sendMail(subject='程序完成情况',msg='您的程序已经运行完成，请去AI Studio查看日志结果',to_list=['603329354@qq.com'])
