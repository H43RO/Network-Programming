import socket
import threading
import time

clients = []
PORT = 4567
BUF_SIZE = 1024


def server_task(sock):
    while True:
        data = sock.recv(BUF_SIZE)

        # Quit 요청한 연결은 끊음
        if 'quit' in data.decode() and sock in clients:
            print(sock, ': exited')
            clients.remove(sock)
            continue

        print(time.asctime() + str(sock) + ':' + data.decode())

        # 송신 측 소켓 제외 나머지 모든 Client 들에게 메세지 전달
        for x in clients:
            if x != sock:
                x.send(data)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(3)

print('=' * 20 + 'Server Started' + '=' * 20)

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print(conn, ': connected')
    threading.Thread(target=server_task, args=(conn,)).start()
