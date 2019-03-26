# coding: utf-8
from bs4 import BeautifulSoup
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from re_html import yuanzun


if __name__ == "__main__":

    Yuanzun = yuanzun()
    titles, urls = Yuanzun.all_url("https://www.qu.la/book/3137/")
    names, contents  = Yuanzun.updata(2, "https://www.qu.la/book/3137/")

    sender = ''			#发送邮箱
    receiver = ''		#接受邮箱
    # subject = 'the first mail'
    # subject = str(name)
    smtpserver = 'smtp.163.com'
    username = ''		#
    password = ''		#

    for i in range(len(names)):
        subject = str(names[i])
        content = contents[i]

        try:
            msg = MIMEText(content, 'plain','utf-8')
            msg['Subject'] = Header(subject, 'utf-8')
            msg['From'] = 'muefornothing@163.com'
            msg['To'] = "594798849@qq.com"	#接受邮箱
            smtp = smtplib.SMTP()
            smtp.connect('smtp.163.com', 25)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
            smtp.quit()
            print("success!")
        except smtplib.SMTPException:
            print("error!")