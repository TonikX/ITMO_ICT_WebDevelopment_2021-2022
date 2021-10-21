import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 7778))
a = input("Введите длину первого катета: ")
b = input("Введите длину второго катета: ")
conn.send(a.encode())
conn.send(b.encode())
c_bin = conn.recv(200)
c = c_bin.decode('utf-8')
print('Гипотенуза треугольника равна: ', c)
conn.close()

