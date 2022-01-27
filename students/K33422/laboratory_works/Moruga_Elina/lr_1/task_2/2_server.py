import socket
import math

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr[0])

# while True:
data = conn.recv(1024)
data = data.decode()

_, url, ver = data.split(" ")
url, params = url.split("?")

params = params.split("&")
params_dct = {}
for param in params:
    p_lst = param.split("=")
    params_dct[p_lst[0]] = float(p_lst[1])


# решение квадратного уравнения

a = params_dct["a"]
b = params_dct["b"]
c = params_dct["c"]
discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    conn.send(("x1 = %.2f \nx2 = %.2f" % (x1, x2)).encode())
elif discr == 0:
    x = -b / (2 * a)
    conn.send(("x = %.2f" % x).encode())
else:
    conn.send("Корней нет".encode())

conn.close()