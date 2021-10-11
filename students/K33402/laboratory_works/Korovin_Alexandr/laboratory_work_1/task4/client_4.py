import socket
from threading import Thread

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))  # подключение к серверу


def send():
    while True:
        conn.send(input().encode("utf-8"))


def accept():
    while True:
        message = conn.recv(16384).decode("utf-8")
        print(message)


Thread(target=send).start()
Thread(target=accept).start()