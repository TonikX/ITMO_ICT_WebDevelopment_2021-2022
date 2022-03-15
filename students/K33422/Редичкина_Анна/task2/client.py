import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 6635))
a = input('Введите длину первого катета: ')
b = input('Введите длину второго катета: ')
catets = ' '.join([str(a), str(b)])
conn.send(catets.encode())
data = conn.recv(1024)
print('Гипотенуза равна: ' + data.decode("utf-8") )
conn.close()


