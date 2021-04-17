import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()  # 클라이언트 소켓, 주소(IP, 포트) 튜플 반환
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    client.close()

