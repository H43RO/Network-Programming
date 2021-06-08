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
content_id = 'my_image1'
msg.add_alternative('''
<html>
    <head></head>
    <body>
        <h1>하이</h1>
        <img src="cid:{cid}"/>
    </body>
</html
'''.format(cid=content_id), subtype='html')


with open('lulu.jpg', 'rb') as img:
    msg.get_payload()[0].add_related(img.read(), maintype='image', subtype='jpg', cid=content_id)

with open('outgoing.msg', 'wb') as f:
    f.write(bytes(msg))


s = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
s.ehlo()
s.starttls()
s.login(sender, password)
s.send_message(msg)
s.quit()
