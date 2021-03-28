import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(3)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    # 이름 수신
    msg = client.recv(1024)
    print(msg.decode())

    # 학번 전송
    id = 20181512
    client.send(id.to_bytes(4, 'big'))

    client.close()
