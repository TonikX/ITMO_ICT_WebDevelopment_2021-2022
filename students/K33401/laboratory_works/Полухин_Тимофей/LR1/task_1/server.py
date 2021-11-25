import socket

server = socket.socket()
host = '127.0.0.1'
port = 8080

server.bind((host, port))
server.listen()

conn, addr = server.accept()
data = conn.recv(16384).decode('utf-8')
print(data)

conn.send(b'Hello, client\n')
conn.close()

