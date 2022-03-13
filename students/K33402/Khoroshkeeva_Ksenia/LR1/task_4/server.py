import socket
from threading import Thread


# Функция для приема сообщений
def send(c):
    while True:
        message = input()
        c.send(message.encode("utf-8"))


# Функция для отправки сообщений
def recieve(c):
    while True:
        data = c.recv(16384)
        print(data.decode("utf-8"))


# Создание сервера
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 5000))
conn.listen(10)

# Подключение клиента
sock, address = conn.accept()

# Запуск функций в отдельных потоках
Thread(target=send, args=[sock]).start()
Thread(target=recieve, args=[sock]).start()
