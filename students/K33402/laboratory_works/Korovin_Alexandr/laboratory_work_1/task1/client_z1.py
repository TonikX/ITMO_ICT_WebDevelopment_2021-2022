import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))  # подключение к серверу

conn.send("Hello server".encode("utf-8"))  # отправляет серверу сообщение

data = conn.recv(16384)
udata = data.decode("utf-8")  # принимает данные
print(udata)
