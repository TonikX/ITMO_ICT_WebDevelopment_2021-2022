import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 15983))
data = conn.recv(1024).decode('utf-8')
print(data)
conn.close()