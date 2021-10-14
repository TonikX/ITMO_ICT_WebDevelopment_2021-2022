import socket
import json
from math import sqrt

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 5000))
conn.listen(5)

while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(4096)
        udata = data.decode('utf-8')
        dict_data = json.loads(udata)
        a, b, c = dict_data

        d = b * b - 4 * a * c
        if d < 0:
            clientsocket.send(b'd < 0; invalid values')
        elif d > 0:
            x1 = (-b + sqrt(d)) / 2 * a
            x2 = (-b - sqrt(d)) / 2 * a
            clientsocket.send(bytes(f'possible x values are {x1}, {x2}', 'utf-8'))
        elif d == 0:
            x = (-b) / 2 * a
            clientsocket.send(bytes(f'x value is {x}', 'utf-8'))

    except KeyboardInterrupt:
        conn.close()
        break

    except Exception as e:
        print(e)
        conn.close()
        break
