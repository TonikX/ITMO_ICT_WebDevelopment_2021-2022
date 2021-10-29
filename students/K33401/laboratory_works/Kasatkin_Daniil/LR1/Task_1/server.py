import random
import socket
import time

server = socket.socket()
host = '127.0.0.1'
port = 8000
server.bind((host, port))
print('Start on:', host, port)
print('URL', (host, port))
server.listen(5)
while True:
    conn, (client_host, client_port) = server.accept()
    print('Got connection', client_host, client_port)
    conn.send(bytes("Hello, client", "utf-8"))
    data = conn.recv(1024)
    conn.send(data)
    print(data.decode('utf-8'))
conn.close()
