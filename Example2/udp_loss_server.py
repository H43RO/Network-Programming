from socket import *
import random

BUF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
print('Listening...')

while True:
    data, addr = sock.recvfrom(BUF_SIZE)
    if random.randint(1, 10) <= 3:
        print(f'Packet from {addr} lost!')
        continue
    print(f'Packet is {data.decode()} from {addr}')

    sock.sendto(b'ack', addr)