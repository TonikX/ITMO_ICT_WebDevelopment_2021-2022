import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))
msg = "Hello, server!"
conn.send(msg.encode("utf-8"))
data = conn.recv(16384)
print(data.decode("utf-8"))
conn.close()
