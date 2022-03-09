import socket

host = "127.0.0.1"
port = 5489
s = socket.socket()
s.bind((host, port))
s.listen(10)

client_sock, client_addr = s.accept()
data = client_sock.recv(16384)
print(data.decode("utf-8"))
client_sock.send(b"Hello, client! \n")
client_sock.close()