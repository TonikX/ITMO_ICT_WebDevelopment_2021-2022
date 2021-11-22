import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 2334))
conn.send(b"Hello, server")

data = conn.recv(1024).decode("utf-8")
print(data)
conn.close()
