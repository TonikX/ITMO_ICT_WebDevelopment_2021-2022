import socket

server = socket.socket()
host = '127.0.0.1'
port = 8080

server.bind((host, port))
server.listen()

conn, addr = server.accept()
a = int(conn.recv(16384).decode('utf-8'))
b = int(conn.recv(16384).decode('utf-8'))
print(a, b, sep='\n')

conn.send(str((a ** 2 + b ** 2) ** (1 / 2)).encode())
conn.close()