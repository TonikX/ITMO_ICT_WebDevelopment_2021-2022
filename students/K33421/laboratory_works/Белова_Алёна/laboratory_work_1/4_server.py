import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8000))
conn.listen(5)
users = []


def send(msg):
    for user in users:
        user.send(msg)


def listen(user):
    while True:
        msg = user.recv(16384)
        send(msg)


def start():
    while True:
        usersocket, address = conn.accept()
        users.append(usersocket)
        listen_user = threading.Thread(target=listen, args=(usersocket,))
        listen_user.start()


start()