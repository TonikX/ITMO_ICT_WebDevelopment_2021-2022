import socket
import math

server = socket.socket()
server.bind(('127.0.0.1', 8000))
server.listen(1)

conn, addr = server.accept()

a = conn.recv(1024).decode('utf-8')
b = conn.recv(1024).decode('utf-8')

c = math.sqrt(int(a) ** 2 + int(b) ** 2)

conn.send(str(c).encode())
conn.close()
