import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 9000))
conn.listen(10)

while True:
    try:
        client_socket, address = conn.accept()
        data = client_socket.recv(16384)
        data = data.decode('utf-8')
        a, b, c = map(float, data.lstrip().rstrip().split())
        print('a =', a)
        print('b =', b)
        print('h =', c)

        discrim = b ** 2 - 4 * a * c
        print("Дискриминант D = %.2f" % discrim)

        if discrim > 0:
            x1 = (-b + math.sqrt(discrim)) / (2 * a)
            x2 = (-b - math.sqrt(discrim)) / (2 * a)
            answ = ("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif discrim == 0:
            x = -b / (2 * a)
            answ = ("x = %.2f" % x)
        else:
            answ = "Корней нет"
        answ = str(answ).encode()
        client_socket.send(answ)

    except KeyboardInterrupt:
        conn.close()
        break