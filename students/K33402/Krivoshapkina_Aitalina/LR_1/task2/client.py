import socket

sock = socket.socket()
sock.connect(('', 1030))

print('Поиск площади трапеции')
a = input('Введите длину первого основания: ')
b = input('Введите длину второго основания: ')
c = input('Введите длину высоты: ')

sock.send((a + ',' + b + ',' + c).encode())

data = sock.recv(1024)
sock.close()

print('Площадь трапеции равна: ', data.decode('utf-8'))