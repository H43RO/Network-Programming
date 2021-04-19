from socket import *
import sys

BUF_SIZE = 1024
LENGTH = 20

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

# 'Hello' 를 보냄으로써 파일 송수신 통신 시작
s.send(b'Hello')

# 서버가 정상적으로 메세지를 받았다면, 'Filename' 을 수신했을 것
msg = s.recv(BUF_SIZE)
if not msg:
    s.close()
    sys.exit()
elif msg != b'Filename':
    print('server : ', msg.decode())
    s.close()
    sys.exit()
else:
    print('server : ', msg.decode())

# 요청할 파일 명을 입력하여 서버에 전송
filename = input('Enter a filename : ')
s.send(filename.encode())

# 만약 서버에 파일이 있다면, 서버로부터 파일 크기를 수신했을 것
msg = s.recv(BUF_SIZE)
if not msg:
    s.close()
    sys.exit()
elif msg == b'NoFile':
    print('server : ', msg.decode())
    s.close()
    sys.exit()
else:
    filesize = int.from_bytes(msg, 'big')
    print('server : ', filesize)

rx_size = 0
# 파일 열기 (다운로드 파일 이름 명시)
f = open("Download_" + filename, 'wb')

# 실제 파일 수신 (쪼개서 수신)
while rx_size < filesize:  # 수신 사이즈가 파일 사이즈만큼 될 때 까지
    data = s.recv(BUF_SIZE)  # 20 바이트씩 분할하여 데이터 수신
    if not data:
        break
    f.write(data)  # 파일 쓰기
    rx_size += len(data)  # 수신받은 만큼 수신 사이즈 증가

if rx_size < filesize:  # 정상 수신되지 않았을 때
    s.close()
    sys.exit()

print('Download complete')
s.send(b'Bye')
f.close()
s.close()
