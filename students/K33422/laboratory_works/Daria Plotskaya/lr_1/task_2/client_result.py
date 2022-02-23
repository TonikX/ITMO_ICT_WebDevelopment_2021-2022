import socket

s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 14900))
a = int(input('Введите длину верхнего основания трапеции: '))
b = int(input('Введите длину нижнего основания трапеции: '))
h = int(input('Введите длину высоты трапеции: '))
q = f'{a}{b}{h}'

s.send(bytes(q, 'utf-8'))
data = s.recv(1024)
print(f'Ваш ответ: {data.decode("utf-8")}')
