import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14000))
conn.send(b"Hello, server! \n")
data = conn.recv(1024)
print(data)

conn.close()
