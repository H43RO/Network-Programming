from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9000))
sock.listen(2)

while True:
    client, addr = sock.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    msg = client.recv(1024)
    print(msg.decode())

    num = 20181512
    client.send(num.to_bytes(4, 'big'))

    client.close()
