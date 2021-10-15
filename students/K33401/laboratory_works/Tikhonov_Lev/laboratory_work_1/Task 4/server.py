import socket
from threading import Thread

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 5000))
conn.listen(10)


def send(message, sender):
    for client in clients:
        if sender != client:
            client.send(message)


def listen(client):
    while True:
        message = client.recv(1024)
        send(message, client)


clients = []
while True:
    new_client, _ = conn.accept()
    if new_client not in clients:
        clients.append(new_client)
    Thread(target=listen, args=[new_client]).start()