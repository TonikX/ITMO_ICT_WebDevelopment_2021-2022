import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))
conn.send(b"Hello, server! \n")
data = conn.recv(16384).decode("utf-8")
print("data: ", data)
conn.close()
