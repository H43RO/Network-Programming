import asyncio
from socket import *

port = 2500
BUF_SIZE = 1024


async def handler(conn, addr):
    while True:
        data = await loop.run_in_executor(None, conn.recv, BUF_SIZE)
        if not data:
            break
        print(f'{addr} Received Mesage: ', data.encode())
        conn.send(data)


async def main():
    sock = socket()
    sock.bind(('', port))
    sock.listen(5)
    while True:
        client, addr = await loop.run_in_executor(None, sock.accept)
        print(addr, 'accepted')
        loop.create_task(handler(client, addr))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()