from socket import *

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('google.com', 80))

socket.send(b'GET / HTTP/1.1\r\n\r\n')

data = socket.recv(10000)
print(data.decode())

socket.close()