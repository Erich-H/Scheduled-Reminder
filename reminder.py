import smtplib
import secrets_1 as secret

message = """From: From Reminder 
To: Me
Subject: Study Reminder 

Its 7:00pm, Time to study for 2 hours. Lets go!
"""

# host - the host running the smtp server, specify ip addres or domain name
# port - providing host argumentm then you need to specify a port where SMTP server is listening
# localhostname - smtp server is running on the local machine 


def send_email():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.starttls()
    smtpObj.login( secret.emailaddr, secret.noclue )
    smtpObj.sendmail(secret.emailaddr, secret.recaddr, message)
    print("Sent the reminder")

    smtpObj.quit()

send_email()