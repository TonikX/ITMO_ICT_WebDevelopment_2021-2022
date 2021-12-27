import socket

server = socket.socket()
host = '127.0.0.1'
port = 7896

server.bind((host, port))
server.listen()

conn, addr = server.accept()
a = int(conn.recv(16384).decode('utf-8'))
b = int(conn.recv(16384).decode('utf-8'))
c = int(conn.recv(16384).decode('utf-8'))
print(a, b, c, sep='\n')


def solving(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 0
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2

conn.send(str(solving(a, b, c)).encode())
conn.close()
