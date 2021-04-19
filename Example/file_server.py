from socket import *
import os

BUF_SIZE = 1024
LENGTH = 4

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(10)

print('File server is running ... ')

while True:
    conn, addr = sock.accept()
    # 'Hello' 수신했을 때
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    elif msg != b'Hello':
        print('client : ', addr, msg.decode())
        conn.close()
        continue
    else:
        print('client : ', addr, msg.decode())

    # 파일 명 요청 메세지 전송
    conn.send(b'Filename')
    # 요청파일명 수신
    msg = conn.recv(BUF_SIZE)
    if not msg:
        conn.close()
        continue
    filename = msg.decode()
    print('client : ', addr, filename)

    try:
        filesize = os.path.getsize(filename)
    except:
        conn.send(b'NoFile')
        conn.close()
        continue
    else:
        # 파일 크기 전송
        fs_binary = filesize.to_bytes(LENGTH, 'big')
        conn.send(fs_binary)

    # 파일 열고 전송 (버퍼 남김없이)
    f = open(filename, 'rb')
    data = f.read()
    conn.sendall(data)

    # 'Bye' 메세지 수신
    msg = conn.recv(BUF_SIZE)
    if not msg:
        pass
    else:
        print('client : ', addr, msg.decode())

    f.close()
    conn.close()
