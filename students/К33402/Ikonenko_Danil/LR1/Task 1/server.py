import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 3228))
conn.listen(10)

sock, address = conn.accept()
data = sock.recv(16384)
data = data.decode("utf-8")
print(data)
msg = "Hello, client!"
sock.send(msg.encode("utf-8"))
conn.close()
