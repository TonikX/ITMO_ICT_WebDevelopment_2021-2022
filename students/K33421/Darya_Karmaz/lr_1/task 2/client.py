import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8001))
conn.send(input("Введите сторону параллелограмма и высоту ").encode())
data = conn.recv(16384)
data = data.decode("utf-8")
print('Площадь параллелограмма:', data)
conn.close()
