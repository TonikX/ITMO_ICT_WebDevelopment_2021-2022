import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9000))

# sending message to server
conn.send(b'Hello server! \n')

# receiving server's response
data = conn.recv(16384)
data = data.decode('utf-8')
print(data)

conn.close()
