import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1', 5000))

conn.send('request'.encode('utf-8'))
data = conn.recv(4096)
udata = data.decode('utf-8')
print(udata)
