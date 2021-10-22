import socket

conn = socket.socket()

conn.connect(('127.0.0.1', 8080))

print(conn.recv(16384).decode())

conn.close()
