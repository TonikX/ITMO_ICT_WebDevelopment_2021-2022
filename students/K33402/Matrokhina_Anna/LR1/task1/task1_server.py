import socket

server = socket.socket()
server.bind(('127.0.0.1', 8000))
server.listen(1)

conn, addr = server.accept()

data = conn.recv(2000)
print(data.decode('utf-8'))

conn.send('Hello, client!'.encode())
conn.close()
