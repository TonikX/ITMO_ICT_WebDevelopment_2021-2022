import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))
conn.send(b"Hello, server!")

data = conn.recv(16384)
udata = data.decode("utf-8")
print("Received answer: " + udata + "\n")

conn.close()
