import socket, threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2235))
s.listen(1)

clients = []
usernames = []

def send_data(msg, current_user):
    for client in clients:
        if client != current_user:
            client.send(msg)


def listen_user(client):
    while True:
        try:
            msg = client.recv(2048)
            send_data(msg, client)

        except ConnectionResetError:

            i= clients.index(client)
            clients.remove(client)
            client.close()

            username = usernames[i]
            send_data(f'{username} left'.encode('utf-8'), username)
            usernames.remove(username)
            break

def start_server():
    while True:
        client, addr = s.accept()
        print(f"Client <{addr[0]}> connected!")
        client.send('nickname'.encode())
        nick = client.recv(2048).decode("utf-8")
        clients.append(client)
        usernames.append(nick)
        client.send('Connected\n'.encode())
        listen_thread = threading.Thread(target=listen_user, args=(client,))
        listen_thread.start()

if __name__ == '__main__':
    start_server()