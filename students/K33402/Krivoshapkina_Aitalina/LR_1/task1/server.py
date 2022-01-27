import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()

print('connected:', addr)

data = conn.recv(1024)
print(data.decode())

conn.send(b'Hello, client')

conn.close()