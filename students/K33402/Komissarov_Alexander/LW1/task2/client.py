#client

import socket
import time


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 10203))
print("Введите длины двух катетов прямоугольного треугольника через пробел:")
raw_input=str(input()).encode()
conn.send(raw_input)
data = conn.recv(9988)
data = data.decode('utf-8')
print(data)
conn.close()
time.sleep(55)
