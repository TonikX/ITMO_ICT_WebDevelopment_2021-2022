import socket

# Подключение к серверу
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 5000))

# Ввод данных с клавиатуры
a = input("Введите длину нижнего основания трапеции: ")
b = input("Введите длину верхнего основания трапеции: ")
h = input("Введите высоту трапеции: ")

# Создание сообщения и отправка трех чисел одним сообщением
message = a + " " + b + " " + h
conn.send(message.encode("utf-8"))

# Получение ответа и вывод в консоль
data = conn.recv(16384)
print(data.decode("utf-8"))

# Закрытие соединения
conn.close()
