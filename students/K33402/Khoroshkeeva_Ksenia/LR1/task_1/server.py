import socket

# Создание сервера
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 5000))
conn.listen(10)

# Прием подключения
sock, address = conn.accept()

# Получение сообщения и вывод в консоль
data = sock.recv(16384)
print(data.decode("utf-8"))

# Создание ответа и отправка
message = "Hello, client"
sock.send(message.encode("utf-8"))

# Закрытие соединения
conn.close()
