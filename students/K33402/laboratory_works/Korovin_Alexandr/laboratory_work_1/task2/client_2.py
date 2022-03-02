import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))  # подключение к серверу

a = input("Введите стороны треугольника через запятую: ")

conn.sendall(a.encode("utf-8"))  # отправляет серверу сообщение

data = conn.recv(16384)
print(data.decode("utf-8"))  # принимает данные
conn.close()
