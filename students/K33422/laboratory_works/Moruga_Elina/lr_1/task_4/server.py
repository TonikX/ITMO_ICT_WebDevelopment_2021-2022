import socket
from threading import Thread

server = socket.socket(socket.AF_INET, 
                       socket.SOCK_STREAM, 
                       proto=0)
host = "localhost"
port = 9090
 
server.bind((host, port))
server.listen(10)
print("Server started.")

clients = []
names = []

def send_message(client_name, data):
    for i, client in enumerate(clients):
        if client_name != names[i]:
            client.send(f"({client_name}): ".encode() + data)

def listen_client(socket):
    while True:
        data = socket.recv(1024) 

        client_name = names[clients.index(socket)]
        print(f"User sent {data}")
        send_message(client_name, data)

def server_accept():
    while True:
        socket, addr = server.accept() 

        # получить имя клиента
        data = socket.recv(1024)
        names.append(data.decode())
            
        print(f"Client {addr[0]}, {addr[1]}, {data.decode()} connected!") 

        clients.append(socket)
        listen_clients = Thread(target=listen_client, args=(socket,))
        listen_clients.start()


server_accept()