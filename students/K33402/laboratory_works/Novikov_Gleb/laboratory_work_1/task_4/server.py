import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5050

server = (host, port)
s = socket.socket()
s.bind(server)
s.listen()
print("[ Server Started ]")

clients = []


def trd(conn):
    while True:
        msg = conn.recv(1024)
        for client, addr in clients:
            client.send(msg)


while True:
    conn, addr = s.accept()
    if addr not in clients:
        clients.append((conn, addr))

    msg = conn.recv(1024)
    print(msg.decode("utf-8"))

    for client, addr in clients:
        client.send(msg)

    threading.Thread(target=trd, args=(conn,)).start()
