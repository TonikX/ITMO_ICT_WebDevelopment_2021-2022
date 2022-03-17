import socket

host = "127.0.0.1"
port = 9091
s = socket.socket()
s.bind((host, port))
s.listen(10)

client_sock, client_addr = s.accept()
data = client_sock.recv(16384)
a, b, h = data.decode("utf-8").split()
area = (int(a) + int(b)) / 2 * int(h)
response = str(area)
client_sock.send(response.encode("utf-8"))
client_sock.close()