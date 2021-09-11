import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 5667))
data = conn.recv(12446)
print(data.decode("utf-8"))
conn.close()