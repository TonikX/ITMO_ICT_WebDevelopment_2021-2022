import math
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14000))

conn.listen(10)

while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(1024)
        udata = data.decode("utf-8")
        a, b = udata.split(" ")
        c = math.sqrt(int(a) ** 2 + int(b) ** 2)

        print(c)

        clientsocket.sendall(str(c).encode())
    except KeyboardInterrupt:
        conn.close()
        break
