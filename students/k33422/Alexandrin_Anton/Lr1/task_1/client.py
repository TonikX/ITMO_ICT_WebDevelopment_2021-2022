import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 5000))

conn.send(b'Hello, server')
data = conn.recv(4096)
udata = data.decode('utf-8')
print(udata)

conn.close()
