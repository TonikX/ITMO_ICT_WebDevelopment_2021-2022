import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 555
server.bind((host,port))
server.listen()

clients = []
cnames = []

print('Starting server on', host, port)

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            cname = cnames[index]
            broadcast(f'{cname} has left the chat room'.encode('utf-8'))
            cnames.remove(cname)
            break

def receive():
    while True:
        client, (c_host, c_port) = server.accept()
        client.send('cname'.encode("utf-8"))
        cname = client.recv(1024)
        cnames.append(cname)
        clients.append(client)
        print(f'This client is {cname}'.encode("utf-8"))
        broadcast(f'{cname.decode("utf-8")} has joined to chat room'.encode("utf-8"))
        client.send('You are now connected.'.encode("utf-8"))
        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()
if __name__ == "__main__":
    receive()
