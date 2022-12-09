import socket

conn = socket.socket()

conn.connect(('127.0.0.1', 7896))

conn.send(b'Hello, server\n')

print(conn.recv(16384).decode('utf-8'))

conn.close()