
import smtplib
from email.mime.text import MIMEText
# smtp服务器
smtpserver = 'pop.qq.com'
# 发送方信息
user = "1269910409@qq.com"
passwd = 'hogwnnpucubngghb'
# 接收方信息
receiver = 'henandzq123@qq.com'
message = MIMEText("我是 通过Python发送的", "plain", "utf-8")
message["from"] = user
message["to"] = receiver
message["subject"] = "测试邮件"
server = smtplib.SMTP(host=smtpserver, port=995)
server.login(user, passwd)
server.sendmail(from_addr=user, to_addrs=receiver, msg=message.as_string())
server.quit()
print("finish")


# import smtplib
# from email.mime.text import MIMEText
# sender = "1269910409@qq.com"
# receiver="2475305686@qq.com"
# passwd = '我的16位密码'
#
# try:
#     smtp = smtplib.SMTP("smtp.qq.com",port=25)
#
#     smtp.login(sender,passwd)
#     # 构造发送消息
#     msg = MIMEText("ssss")
#     msg["from"] = sender
#     msg["to"] = receiver
#     msg["subject"] = "测试邮件"
#     smtp.sendmail(sender, receiver, msg.as_string())
#     smtp.quit()
# except Exception as e:
#     print(e)
