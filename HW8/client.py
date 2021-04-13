from socket import *

PORT = 333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send [mBoxID] message" or "receive [mBoxID] : ')
    if msg.startswith('send'):  # ID 와 Message 전송
        sock.sendto(msg.encode(), ('localhost', PORT))
        print('OK')
    elif msg.startswith('receive'):  # ID 만 전송
        sock.sendto(msg.encode(), ('localhost', PORT))
        data, addr = sock.recvfrom(BUFF_SIZE)
        print(data.decode())
    elif msg == 'quit':
        sock.sendto('quit'.encode(), ('localhost', PORT))
        break
    else:
        print('Invalid Input')

sock.close()
