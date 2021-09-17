import socket
soc = socket.socket()
soc.connect(('localhost',9090))
msg = input()
soc.send(bytes(msg, "utf8"))
data = soc.recv(1024)
print(data.decode('utf8'))
soc.close()