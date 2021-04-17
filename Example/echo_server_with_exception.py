from socket import *

port = 2500
BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

conn, (remotehost, remortport) = sock.accept()
print('Connected By', remotehost, remortport)

while True:
    try:
        data = conn.recv(BUF_SIZE)
    except:
        break
    else:
        if not data:
            break
        print("Received Message : ", data.decode())
    try:
        conn.send(data)
    except:
        break

conn.close()