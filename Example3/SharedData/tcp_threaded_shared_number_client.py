from socket import *

port = 2500
BUF_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', port))

print(int(s.recv(BUF_SIZE).decode()))

s.close()