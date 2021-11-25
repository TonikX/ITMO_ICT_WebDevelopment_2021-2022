import socket
import threading

PORT = 7000
HOST = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((HOST, PORT))
except socket.error as e:
    print(str(e))

print("........")
sock.listen(5)

clients = []
names = []

def send_mess(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            send_mess(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            names.remove(names[index])
            break

def thread_client():
    while True:
        client, addr = sock.accept()
        print("Connected with " + str(addr))
        client.send("NAME".encode('utf-8'))
        name = client.recv(1024).decode('utf-8')
        names.append(name)
        clients.append(client)
        print("Name is " + name)
        send_mess("{} joined. \n".format(name).encode('utf-8'))
        client.send("Connected to server.".encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client, ))
        thread.start()

thread_client()