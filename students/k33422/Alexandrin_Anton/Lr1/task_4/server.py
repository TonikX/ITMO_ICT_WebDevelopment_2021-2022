import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 5002))
server.listen()

clients = []
usernames = []


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(4096)
            broadcast(message)

        except Exception as e:
            print('Exception:', e)
            index = clients.index(client)
            clients.remove(client)
            client.close()

            username = usernames[index]
            broadcast(f'{username} left'.encode('utf-8'))
            usernames.remove(username)
            break


def receive():
    while True:
        try:
            client, client_address = server.accept()
            print(f'accepted connection from {client_address}')

            client.send('NICKNAME'.encode('utf-8'))
            username = client.recv(4096).decode('utf-8')
            clients.append(client)
            usernames.append(username)
            broadcast(f'{username} joined'.encode('utf-8'))

            handle_thread = threading.Thread(target=handle, args=(client,))
            handle_thread.start()

        except Exception as e:
            print('Exception:', e)
            broadcast(f'')


receive()
