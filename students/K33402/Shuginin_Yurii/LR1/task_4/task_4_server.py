import socket
import threading

def display_msg(author, msg):
    for client in clients:
        if author != client:
            client.send(msg.encode())


def client_handler(sock, address):
    print(f"{address[0]}:{address[1]} connected")
    
    while True:
        message = sock.recv(16384).decode("utf-8")
        if len(message) == 0:
            break
        message = f"{address[0]}:{address[1]}: " + message
        display_msg(sock, message)
    
    print(f"{address[0]}:{address[1]} disconnected")
    clients.remove(sock)
    sock.close()


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("127.0.0.1", 9090)
serversocket.bind(server_address)
serversocket.listen(100)
clients = []

print(f"Starting Chat Server at {server_address[0]}:{server_address[1]}")
try:
    while True:
        clientsocket, client_address = serversocket.accept()
        if clientsocket not in clients:
            clients.append(clientsocket)
        client_thread = threading.Thread(target=client_handler, args=(clientsocket, client_address))
        client_thread.start()

except KeyboardInterrupt:
    print("\n" + "Shutting down" + "\n")
    serversocket.close()
