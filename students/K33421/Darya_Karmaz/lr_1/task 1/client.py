import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 800))
conn.send(b"Hello, server")

data = conn.recv(16384)
data = data.decode("utf-8")
conn.close()
print(data)
