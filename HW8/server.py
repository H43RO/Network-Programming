from socket import *
from collections import deque

PORT = 333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', PORT))
box = {}

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)
    request = data.decode()

    if request.startswith('send'):
        temp = list(request.split())
        box_id, message = temp[1], temp[2:]
        message = " ".join(message)
        if box_id not in box:
            print(f'{box_id} 박스가 생성되었습니다.')
            box[str(box_id)] = deque(["".join(message)])
            print(f'{box_id} 박스에 {message} 가 담겼습니다')
        else:
            box[str(box_id)].append("".join(message))
            print(f'{box_id} 박스에 {message} 가 담겼습니다')

    elif request.startswith('receive'):
        box_id = request.split()[1]
        if box_id not in box:
            print(f'{box_id} 박스 자체가 없습니다')
            sock.sendto("No messages".encode(), addr)
        else:
            if box[str(box_id)]:
                print(f'{box_id} 박스에 메세지가 담겨 있으므로 전송합니다')
                sock.sendto(box[str(box_id)].popleft().encode(), addr)
            else:
                print(f'{box_id} 박스에 메세지가 없습니다')
                sock.sendto("No messages".encode(), addr)
