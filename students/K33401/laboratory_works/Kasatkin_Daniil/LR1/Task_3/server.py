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
    page = open('index.html')
    content = page.read()
    page.close()
    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.sendall(response.encode())
conn.close()
