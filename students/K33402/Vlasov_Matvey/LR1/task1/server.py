import socket

conn = socket.socket()
conn.bind(("127.0.0.1", 2334))
conn.listen(1)

client, (client_host, client_port) = conn.accept()
data = client.recv(1024).decode("utf-8")
print(data)
client.send(b"Hello, client")
conn.close()
