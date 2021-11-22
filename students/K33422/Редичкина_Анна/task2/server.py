#Теорема Пифагора
import math
import socket

sock = socket.socket()
sock.bind(("", 6635))
sock.listen(10)
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    udata = data.decode("utf-8")
    a, b = udata.split()
    c = math.sqrt(int(a) ** 2 + int(b) ** 2)
    print(f"Первый катет равен {a}, второй равен {b}")
    if not data:
        break
    conn.send(str(c).encode())
conn.close()

