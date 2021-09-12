import socket

server = socket.socket()
host = '127.0.0.1'
port = 7777
server.bind((host, port))
server.listen(1)

conn, addr = server.accept()
data = conn.recv(2000)
udata = data.decode('utf-8')
print(udata)
conn.send(b"Hello, client! \n")
conn.close()

