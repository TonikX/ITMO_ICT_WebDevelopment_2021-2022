import socket
import math
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9000))

# sending message to server
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

answ = ' '.join([str(a), str(b), str(c)]).encode()
conn.send(answ)

data = conn.recv(16384)
data = data.decode('utf-8')
print('Решение квадратного уравнения: ', data)

conn.close()