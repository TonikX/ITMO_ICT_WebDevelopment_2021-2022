import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 65432))
    s.listen(3)
    connection, address = s.accept()
    side = int(connection.recv(1024).decode('utf-8'))
    height = int(connection.recv(1024).decode('utf-8'))
    connection.send(str(side*height).encode())