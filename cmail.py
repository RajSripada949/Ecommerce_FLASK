import smtplib
from smtplib import SMTP 
from email.message import EmailMessage

def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("raj20241a05t0@grietcollege.com","hgfd jazr jfei dalm")
    msg=EmailMessage()
    msg['From']='raj20241a05t0@grietcollege.com'
    msg['Subject']=subject
    msg['To']='sripadaraj77@gmail.com'
    msg.set_content(body)
    server.send_message(msg)
    server.quit()