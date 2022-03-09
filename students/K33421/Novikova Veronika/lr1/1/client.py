import socket

host = "127.0.0.1"
port = 5489

s = socket.socket()
s.connect((host, port))
s.send(b"Hello, server! \n")

data = s.recv(16384)
print(data.decode("utf-8"))

s.close()