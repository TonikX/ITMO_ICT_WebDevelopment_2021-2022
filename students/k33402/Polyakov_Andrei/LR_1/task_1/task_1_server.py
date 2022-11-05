import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 5667))
sock.listen(1)
conn, address = sock.accept()
data = conn.recv(12446)
print(data.decode("utf-8"))
conn.send(b"Hello, client \n")
conn.close()
