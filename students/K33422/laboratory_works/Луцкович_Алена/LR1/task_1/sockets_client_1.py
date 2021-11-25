import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 7777))
conn.send(b"Hello, server! \n")
data = conn.recv(2000)
udata = data.decode('utf-8')
print(udata)
conn.close()

