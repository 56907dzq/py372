import smtplib
from email.mime.text import MIMEText
sender = "1269910409@qq.com"
receiver="2475305686@qq.com"
passwd = 'hogwnnpucubngghb'

try:
    smtp = smtplib.SMTP("smtp.qq.com",port=25)

    smtp.login(sender,passwd)
    # 构造发送消息
    msg = MIMEText("ssss")
    html = "<h1>标题1</h1> 我是 通过Python发送的1 <i>作者</i>"
    msg = MIMEText(html, 'html')
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = "测试邮件"
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
except Exception as e:
    print(e)
