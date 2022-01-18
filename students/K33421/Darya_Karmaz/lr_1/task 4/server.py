import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 5000))
conn.listen(10)
users = []


def send_messages(data, author):
    for user in users:
        if author != user:
            user.send(data)


def accept_messages(user):
    while True:
        data = user.recv(16384)
        send_messages(data, user)


while True:
    try:
        clientsocket, address = conn.accept()
        users.append(clientsocket)
        accepting_thread = threading.Thread(target=accept_messages, args=(clientsocket,))
        accepting_thread.start()
    except KeyboardInterrupt:
        conn.close()
        break
