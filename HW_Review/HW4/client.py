from socket import *

sock = socket(AF_INET, SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

msg = sock.recv(1024)
print(msg.decode())

sock.send(b'Kim HyunJun')
msg = sock.recv(1024)
msg = int.from_bytes(msg, 'big')
print(msg)

sock.close()