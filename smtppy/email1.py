import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com",port=25)

sender="1269910409@qq.com"
receiver="2475305686@qq.com"
smtp.login(sender, "hogwnnpucubngghb")

msg="nenglianshangma"
text_plain=MIMEText(msg,"plain","utf-8")
smtp.sendmail(sender, receiver, text_plain.as_string())
smtp.quit()