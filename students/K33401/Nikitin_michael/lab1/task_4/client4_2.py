import socket, sys
from threading import Thread

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 53331))
print("Connected to chat")


def messenger():
    while True:
        message = input()
        if message == "exit":
            sock.send(message.encode())
            sock.close()
            sys.exit()
        else:
            sock.send(message.encode())


def receiver():
    while True:
        data = sock.recv(4096)
        if data:
            print(data.decode())


message_thread = Thread(target=messenger)
get_thread = Thread(target=receiver)

message_thread.start()
get_thread.start()