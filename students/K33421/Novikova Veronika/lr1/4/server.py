import socket
import threading

s = socket.socket()
host = "127.0.0.1"
port = 5556
s.bind((host, port))
s.listen()

clients = []
users = []

def broadcast(message, client):
    for i in clients:
        if i != client:
            i.send(message)

def handle(client):
    while True:
        message = client.recv(16384)
        if message.decode("utf-8") == 'close':
            i = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[i]
            users.remove(user)
            message = '{} left chat'.format(user).encode("utf-8")
            broadcast(message, client)
            break
        broadcast(message, client)

def recieve():
    while True:
        client_sock, client_addr = s.accept()
        client_sock.send('username?'.encode('utf-8'))
        user = client_sock.recv(16384).decode('utf-8')
        users.append(user)
        clients.append(client_sock)
        client_sock.send("Type 'close' to leave chat".encode('utf-8'))
        broadcast('Say hi to {}'.format(user).encode("utf-8"), client_sock)
        thread = threading.Thread(target=handle, args=(client_sock,))
        thread.start()

recieve()
