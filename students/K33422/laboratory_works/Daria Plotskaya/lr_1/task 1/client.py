import socket

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 14900))
msg = s.recv(1024)
s.send(bytes("Hello, server", "utf-8"))

print(msg.decode('utf-8'))
