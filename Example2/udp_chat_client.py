from socket import *

port = 3333
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    sock.sendto(msg.encode(), ('localhost', port))

    data, addr = sock.recvfrom(BUF_SIZE)
    print('<- ', data.decode())
