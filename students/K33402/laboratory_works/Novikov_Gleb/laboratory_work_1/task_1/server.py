import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 5000))
conn.listen(10)

client_socket, address = conn.accept()
data = client_socket.recv(16384)
data = data.decode('utf-8')
print(data)

client_socket.send(b'Hello client! \n')
conn.close()
