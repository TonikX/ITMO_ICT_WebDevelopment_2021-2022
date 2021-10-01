import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9900))
sock.send(b"Hello, server!\n")

data = sock.recv(1024)
udata = data.decode("utf-8")
print(udata)
sock.close()