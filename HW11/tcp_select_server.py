import socket, select
import time

socks = []
BUF_SIZE = 1024
PORT = 1234

s_sock = socket.socket()
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print('=' * 20 + 'Server Started' + '=' * 20)

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])

    for s in r_sock:
        if s == s_sock:
            conn, addr = s_sock.accept()
            socks.append(conn)
            print(f'Client ({addr} connected.')
        else:
            data = s.recv(BUF_SIZE)

            if 'quit' in data.decode():
                s.close()
                socks.remove(s)
                continue

            print(time.asctime() + str(s.getsockname()) + ':' + data.decode())

            for client in socks:
                if client != s and client != s_sock:
                    client.send(data)
