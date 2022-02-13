import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 3228))
conn.listen(10)

sock, address = conn.accept()
sock.send("Введите длину основания параллелограмма:".encode())
b = int(sock.recv(16384).decode())
sock.send("Введите высоту параллелограмма:".encode())
h = int(sock.recv(16384).decode())
area = b * h
sock.send(f"Площадь параллелограмма равна:\n{b} x {h} = {area}".encode())
conn.close()

# Вариант D
