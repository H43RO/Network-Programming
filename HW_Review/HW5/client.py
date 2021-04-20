from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    op = input("수식을 입력하세요 (사칙연산 지원) : ")
    if op == 'q':
        break
    s.send(op.encode())

    print('Result : ', s.recv(1024).decode())

s.close()