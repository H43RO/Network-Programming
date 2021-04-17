import MyTCPServer as my

port = 2500
BUF_SIZE = 1024

sock = my.TCPServer(port)
conn, addr = sock.Accept()

print('connected by ', addr)

while True:
    data = conn.recv(BUF_SIZE)
    if not data:
        break
    print("Received Message : ", data.decode())
    conn.send(data)

conn.close()
