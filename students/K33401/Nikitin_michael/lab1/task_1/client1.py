import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 14900))
sock.sendall(b'Hello, server!')

data = sock.recv(16384)
print(data.decode("utf-8"))

sock.close()
