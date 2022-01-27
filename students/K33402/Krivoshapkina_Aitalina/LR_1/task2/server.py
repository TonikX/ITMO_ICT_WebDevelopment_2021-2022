import socket

host = socket.gethostbyname(socket.gethostname())
port = 1030

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)

conn, addr = sock.accept()
print('connected:', addr)
data = conn.recv(1024).decode('utf-8')

data = data.split(',')
a = data[0]
b = data[1]
c = data[2]

S = 0.5*(int(a)+int(b))*int(c)
print(S)

conn.send(str(S).encode())
conn.close()
