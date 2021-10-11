import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))  # сервер занимает такой адрес
conn.listen(10)

clientsocket, address = conn.accept()  # сервер подключает клиента

data = clientsocket.recv(16384)
udata = data.decode("utf-8")  # принимает данные
print(udata)

data = "Hello client".encode("utf-8")  # отправляет клиенту сообщение
clientsocket.send(data)

conn.close()
