import csv
import smtplib
from email.mime.text import MIMEText

gmail_user = 'your-gmail-id@gmail.com'  # Type your gmail ID
gmail_password = 'your-gmail-password'  # Type your gmail password

with open('mail-content.txt') as txtfile:
    content = txtfile.read()


def send_mail_one_receiver(receiver):
    msg = MIMEText(content)
    msg['Subject'] = 'your-mail-subject'  # Type your mail subject
    msg['From'] = gmail_user
    msg['To'] = receiver
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.send_message(msg)
    server.quit()


with open('mail-list.csv') as csvfile:
    rows = csv.reader(csvfile)
    for receiver in rows:
        send_mail_one_receiver(receiver[0])
    print('Email sent!')
