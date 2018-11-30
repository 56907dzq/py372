import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
sender = "1269910409@qq.com"
receiver="2475305686@qq.com"
passwd = 'hogwnnpucubngghb'

try:
    smtp = smtplib.SMTP("smtp.qq.com",port=25)

    smtp.login(sender,passwd)
    # 构造发送消息
    # msg = MIMEText("ssss")
    # html = "<h1>fujian</h1> 我是 通过Python发送的1 <i>作者</i>"
    # msg = MIMEText(html, 'html')
    # msg = MIMEMultipart()
    # img["Content-Disposition"] = 'attachment,filename="hdrCount.txt"'
    # 这行改为：
    # img["Content-Disposition"] = 'attachment,filename=%s' % string.encode("utf-8")
    # 也就是说对你发送的内容需要进行utf - 8编码

    fileimage = open("e:/123.jpg", 'rb')
    msg=MIMEImage(fileimage.read(),"image")
    fileimage.close()
    msg["from"] = sender
    msg["to"] = receiver
    msg["subject"] = "测试邮件3"
    string="abc.jpg"
    msg["Content-Disposition"] = 'attachment,filename=%s'%string.encode("utf-8")
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
except Exception as e:
    print(e)
    # # 文件附件
    # filedoc = open("d:/zzy.docx", "rb")
    # msgfile = MIMEText(filedoc.read(), "base64", "utf-8")
    # filedoc.close()
    # msgfile["Content-Type"] = 'application/octet-stream'
    # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    # msgfile["Content-Disposition"] = 'attachment; filename="test.docx"'
    # message.attach(msgfile)
