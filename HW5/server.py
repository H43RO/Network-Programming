from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('Waiting...')

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break
        try:
            a, op, b = data.decode().split()
            if op == '+':
                result = int(a) + int(b)
            elif op == '-':
                result = int(a) - int(b)
            elif op == '*':
                result = int(a) * int(b)
            else:
                result = round(float(a) / float(b), 1)
        except:
            client.send(b'Try Again')
        else:
            client.send(str(result).encode())

    client.close()