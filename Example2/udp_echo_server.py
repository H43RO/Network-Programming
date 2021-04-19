import socket

port = 2500
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

while True:
    msg, addr = sock.recvfrom(BUF_SIZE)
    print('Received : ', msg.decode())

    sock.sendto(msg, addr)

