import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 5667))
a, b = input("Введите стороны треугольника через запятую: ").split(",")
conn.sendall(bytes(f'{a}, {b}', "utf-8"))
data = conn.recv(12446)
print(data.decode("utf-8"))
conn.close()