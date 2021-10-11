import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))  # сервер занимает такой адрес
conn.listen(1)

while True:
    try:
        clientsocket, address = conn.accept()  # сервер подключает клиента
        data = clientsocket.recv(16384)
        a, b = data.decode("utf-8").split(",")  # принимает данные
        answer = str(math.sqrt(int(a) ** 2 + int(b) ** 2))
        clientsocket.send(answer.encode("utf-8"))
        clientsocket.close()
    except KeyboardInterrupt:
        conn.close()
