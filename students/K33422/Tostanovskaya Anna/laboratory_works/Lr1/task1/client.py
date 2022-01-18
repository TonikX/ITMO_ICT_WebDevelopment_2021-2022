import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))

client_message = "Hello, server!"
conn.send(bytes(client_message, "utf-8"))
data_recv = conn.recv(1024)
data_recv = data_recv.decode('utf-8')
print(("Data received: " + data_recv))

conn.close()