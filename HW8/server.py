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
            box[str(box_id)] = deque([message])
            print(f"LOG : [{box_id}] <- '{message}'")
        else:
            box[str(box_id)].append(message)
            print(f"LOG : [{box_id}] <- '{message}'")

    elif request.startswith('receive'):
        box_id = request.split()[1]
        if box_id not in box:
            print(f"LOG : [{box_id}] box doesn't exist -> send failed")
            sock.sendto("No messages".encode(), addr)
        else:
            if box[str(box_id)]:
                print(f'LOG : [{box_id}] box has message -> send to [{addr}]')
                sock.sendto(box[str(box_id)].popleft().encode(), addr)
            else:
                print(f'LOG : [{box_id}] box has not message -> send failed')
                sock.sendto("No messages".encode(), addr)
