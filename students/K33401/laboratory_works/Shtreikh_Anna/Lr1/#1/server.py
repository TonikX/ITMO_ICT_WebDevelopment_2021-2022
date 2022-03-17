import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 9900))
sock.listen()

conn, addr = sock.accept()
data = conn.recv(1024)
udata = data.decode("utf-8")
print(udata)
conn.send(b"Hello, client! \n")
conn.close()
