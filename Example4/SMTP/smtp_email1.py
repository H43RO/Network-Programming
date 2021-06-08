import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'h2is1234@gmail.com'
recipient = 'mmy789@naver.com'
password = 'jlyunhdywyobtvob'

msg = EmailMessage()
msg['Subject'] = '이메일 테스트'
msg['From'] = sender
msg['To'] = recipient
text = 'ㅇㅅ ㅇ'
msg.set_content(text)

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()