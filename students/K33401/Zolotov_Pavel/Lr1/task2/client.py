import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 65432))
    side = input("Сторона параллелограмма: ")
    height = input("Высота, проведенная к данной стороне: ")
    s.send(side.encode())
    s.send(height.encode())
    data = s.recv(1024).decode('utf-8')
print('Площадь параллелограмма: ', data)