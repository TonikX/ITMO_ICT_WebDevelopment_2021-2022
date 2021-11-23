import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9900))

a = input("Введите значение верхнего основания трпаеции. ").encode('utf-8')
sock.send(a)
b = input("Введите значение нижнего основания трапеции. ").encode('utf-8')
sock.send(b)
h = input("Введите значение высоты трапеции. ").encode('utf-8')
sock.send(h)

s = sock.recv(1024)
print(s.decode("utf-8"))
sock.close()