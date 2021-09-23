import random
import socket
import time
import math

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
    data = conn.recv(1024).decode('utf-8').split(' ')
    data = list(map(int, data))
    response = math.sqrt(data[0] ** 2 + data[1] ** 2)
    conn.send(bytes('Ващ гипотинуза = '+ str(response), "utf-8"))

conn.close()
