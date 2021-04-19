from socket import *

BUF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)
sock.connect(('localhost', port))

for i in range(10):
    time = 0.1
    data = 'Hello, IoT!'
    while True:
        sock.send(data.encode())
        print(f'Packet({i}) : Waiting up to {time} secs for ACK')
        sock.settimeout(time)
        try:
            data = sock.recv(BUF_SIZE)
        except timeout:
            time *= 2
            if time > 2.0:
                break
        else:
            print('Response', data.decode())
            break