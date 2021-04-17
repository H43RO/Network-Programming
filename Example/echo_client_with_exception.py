import socket

port = int(input("PORT NO : "))
address = ("localhost", port)
BUF_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

while True:
    msg = input("Message to send : ")
    try:
        bytes_sent = s.send(msg.encode())
    except:
        print('connection closed')
        break
    else:
        print(f"{bytes_sent} bytes send")

    try:
        data = s.recv(BUF_SIZE)
    except:
        print('connection closed')
        break
    else:
        if not data:
            break
        print("Received Message : %s" %data.decode())