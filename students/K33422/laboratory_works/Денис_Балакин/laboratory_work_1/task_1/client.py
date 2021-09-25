import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 5667))

conn.send(b'Hello my dear server! \n')

data = conn.recv(16384)
data = data.decode('utf-8')
print(data)

conn.close()