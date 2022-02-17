import socket
import threading

HOST, PORT = "127.0.0.1", 14900

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(1)

clients = []
usernames = []

def data_send(msg, user):
    for client in clients:
        if client != user:
            client.send(msg)
    return

def listen_user(client):
    while True:
        try:
            msg = client.recv(16384)
            data_send(msg, client)

        except ConnectionResetError:

            j = clients.index(client)
            clients.remove(client)
            client.close()

            name = usernames[j]
            data_send(f'{name} left'.encode('utf-8'), name)
            usernames.remove(name)
            break

def start_server():
    while True:
        client, adress = conn.accept()
        print(f"Client <{adress[0]}> connected!")
        client.send("name ".encode() )
        nick = client.recv(16384).decode("utf-8")
        clients.append(client)
        usernames.append(nick)
        client.send("Connected\n".encode())
        listen_thread = threading.Thread(target=listen_user, args=(client,))
        listen_thread.start()

if __name__ == '__main__':
    start_server()