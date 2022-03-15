import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '127.0.0.1'
port = 8010
server.bind((host, port))
print('Start on:', host, port)
print('URL', (host, port))
server.listen(100)
list_of_users = []
list_of_clients = set()
separator_token = "<SEP>"

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            list_of_clients.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
        for client in list_of_clients:
            client.send(msg.encode())

while True:
    client, client_address = server.accept()
    print(f"[+] {client_address} connected.")
    list_of_clients.add(client)
    t = Thread(target=listen_for_client, args=(client,))
    t.daemon = True
    t.start()