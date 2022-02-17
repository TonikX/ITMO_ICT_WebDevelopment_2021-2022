import socket

HOST, PORT = "127.0.0.1", 14900

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))
conn.send(b"Hello, server! \n")

data = conn.recv(16384)

conn.close()

udata = data.decode("utf-8")
print(udata)