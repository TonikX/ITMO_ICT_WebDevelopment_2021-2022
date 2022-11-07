import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 8000))

print('Расчет длины гипотенузы по Теореме Пифагора')

a = input('Первый катет: ')
b = input('Второй катет: ')

conn.send(a.encode())
conn.send(b.encode())

c = conn.recv(1024)
print('Гипотенуза треугольника равна: ', c.decode('utf-8'))

conn.close()
