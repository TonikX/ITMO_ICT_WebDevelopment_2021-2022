import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 65432))
    s.listen()
    connection, address = s.accept()
    data = connection.recv(1024).decode('utf-8')
    print(data)
    connection.send(b'Hello, client')