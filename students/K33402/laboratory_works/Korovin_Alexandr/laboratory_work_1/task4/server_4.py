import socket
from threading import Thread

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))  # сервер занимает такой адрес
conn.listen(10)

clientsocket, address = conn.accept()  # сервер подключает клиента


def send():
    while True:
        clientsocket.send(input().encode("utf-8"))


def accept():
    while True:
        message = clientsocket.recv(16384).decode("utf-8")
        print(message)

Thread(target=send).start()
Thread(target=accept).start()