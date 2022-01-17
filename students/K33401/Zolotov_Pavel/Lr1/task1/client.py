import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 65432))
    s.sendall(b'Hello, server')
    data = s.recv(1024).decode('utf-8')
print(data)