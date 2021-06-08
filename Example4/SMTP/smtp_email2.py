import imghdr
import smtplib
from email.message import EmailMessage

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

sender = 'h2is1234@gmail.com'
family = ['mmy789@naver.com', 'mac-pro@kakao.com']
password = 'jlyunhdywyobtvob'

msg = EmailMessage()
msg['Subject'] = '크림히어로즈 루루'
msg['From'] = sender
msg['To'] = ', '.join(family)
text = 'ㅇㅅ ㅇ'
msg.set_content(text)
msg.preamble = '^O A O^'

with open('lulu.jpg', 'rb') as f:
    img_data = f.read()

msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data), filename='lulu.jpg')

s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
