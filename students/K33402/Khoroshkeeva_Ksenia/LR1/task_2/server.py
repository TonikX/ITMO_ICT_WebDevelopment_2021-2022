import socket

# Создание сервера
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 5000))
conn.listen(10)

# Прием подключения
sock, address = conn.accept()

# Получение сообщения и разделение на числа
data = sock.recv(16384)
a, b, h = data.decode("utf-8").split()

# Нахождение площади трапеции по формуле
a = float(a)
b = float(b)
h = float(h)
s = 0.5 * (a + b) * h

# Создание ответа и отправка
message = f"Площадь трапеции равна {s}"
sock.send(message.encode("utf-8"))

# Закрытие соединения
conn.close()
