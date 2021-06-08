import asyncio

port = 2500
BUF_SIZE = 1024


async def main():
    reader, writer = await asyncio.open_connection('localhost', port)

    while True:
        data = input('Enter the message to send : ')
        writer.write(data.encode())
        await writer.drain()

        data = await reader.read(BUF_SIZE)
        print('Received : ', data.decode())


asyncio.run(main())