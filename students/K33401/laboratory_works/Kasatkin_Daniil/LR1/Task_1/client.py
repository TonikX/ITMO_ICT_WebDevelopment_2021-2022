import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 8000))
conn.send(bytes("Hello, server", "utf-8"))
data = conn.recv(1024)
conn.close()    
print(data.decode('utf-8'))
