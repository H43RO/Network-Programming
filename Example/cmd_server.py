from socket import *
import sys

port = 2500
BUF_SIZE = 1024

if len(sys.argv) > 1:
    port = int(sys.argv[1])
    print(port)

socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('', port))
socket.listen(1)

conn, addr = socket.accept()
print('connected by ', addr)

while True:
    data = conn.recv(BUF_SIZE)
    if not data:
        break
    print("Received Message : ", data.decode())
    conn.send(data)

conn.close()