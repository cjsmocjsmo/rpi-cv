import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def charlie():
    email = "porthose.cjsmo.cjsmo@gmail.com"
    pas = "porthose01"
    sms_gateway = '9038201482@mymetropcs.com'
    smtp = "smtp.gmail.com" 
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "PiCam\n"
    body = "Motion Has Been Detected\n"
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    server.sendmail(email,sms_gateway,sms)
    server.quit()



def teresa():
    email = "porthose.cjsmo.cjsmo@gmail.com"
    pas = "porthose01"
    sms_gateway = '9034366799@mymetropcs.com'
    smtp = "smtp.gmail.com" 
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "PiCam\n"
    body = "Motion Has Been Detected\n This is a test"
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    server.sendmail(email,sms_gateway,sms)
    server.quit()

def dylan():
    email = "porthose.cjsmo.cjsmo@gmail.com"
    pas = "porthose01"
    sms_gateway = '3606201169@vtext.com'
    smtp = "smtp.gmail.com" 
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, pas)
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_gateway
    msg['Subject'] = "PiCam\n"
    body = "This is a test of the grandpa motion detection notification system\n"
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    server.sendmail(email,sms_gateway,sms)
    server.quit()

charlie()
teresa()
# dylan()