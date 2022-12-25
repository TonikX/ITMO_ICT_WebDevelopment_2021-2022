# Решение квадратного уравнения
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

sock.send(f'GET https://localhost?a={a}&b={b}&c={c} HTTP/1.1'.encode())

print("Ждем ответ от сервера...")
data = sock.recv(1024)

print(data.decode())

sock.close()