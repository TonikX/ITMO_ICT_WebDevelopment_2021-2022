import socket
soc = socket.socket()
soc.bind(('localhost', 9090))
soc.listen(10)
conn, addr = soc.accept()
print(addr)
a = conn.recv(1024).decode('utf8')
b = conn.recv(1024).decode('utf8')
h = conn.recv(1024).decode('utf8')
ans = str((int(a)+int(b))*int(h))
conn.send(ans.encode())
soc.close()


