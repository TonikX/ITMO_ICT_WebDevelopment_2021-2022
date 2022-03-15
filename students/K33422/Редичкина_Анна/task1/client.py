import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 5635))
conn.send(b"Hello, server! \n")
data = conn.recv(1024)
print(data.decode("utf-8") )
conn.close()

