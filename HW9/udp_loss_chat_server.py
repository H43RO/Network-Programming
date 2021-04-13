from socket import *
import random
import time

PORT = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', PORT))

while True:
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break

    msg = input('-> ')
    reTx = 0
    while reTx <= 3:  # 최대 3회까지 재전송
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        sock.settimeout(2)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    if reTx > 3:
        print('Timeout.')