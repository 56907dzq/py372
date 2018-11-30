import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
serversmtp = "smtp.qq.com"
user = '1269910409@qq.com'
passwd = 'hogwnnpucubngghb'
receiver = '2475305686@qq.com'
try:
    smtp = smtplib.SMTP(serversmtp,port=25)
    smtp.login(user, passwd)
    message = MIMEMultipart()
    # message = MIMEText("我是文本", "plain", "utf-8")
    message["from"] = user
    message["to"] = receiver
    message["subject"] = "带附件邮件"
    # html附件
    html = "<b>图片附件</b><img src='cid:imageid'/>"
    msghtml = MIMEText(html, "html", "utf-8")
    message.attach(msghtml)
    # 图片附件
    fileimage = open("e:/123.jpg", 'rb')
    msgimage = MIMEImage(fileimage.read())
    fileimage.close()
    msgimage.add_header("Content-ID", "imageid")
    message.attach(msgimage)
    smtp.sendmail(user, receiver, message.as_string())
    smtp.quit()
except Exception as e:
    print(e)
