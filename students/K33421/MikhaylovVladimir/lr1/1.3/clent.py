import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
sock.send('Hello, server!'.encode("utf-8"))

data = sock.recv(1024)
sock.close()

print(data.decode("utf-8"))
