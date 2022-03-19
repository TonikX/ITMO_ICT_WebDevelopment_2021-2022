import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 4341))
data = input("Начиная с пробела, введите значения a, b, h: ")
conn.send(data.encode("utf-8"))
result = conn.recv(16384).decode("utf-8")
print("Площадь трапеции = ", result)
conn.close()
