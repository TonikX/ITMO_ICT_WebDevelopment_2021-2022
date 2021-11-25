import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9000))

sockets_list = [sys.stdin, client]

while True:
    try:
        message = input('You: ')
        client.send(message.encode())

        message = client.recv(1024)
        message = message.decode()
        print(message)

    except KeyboardInterrupt:
        client.close()

    except:
        continue
