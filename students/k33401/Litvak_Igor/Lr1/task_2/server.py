# Variant d. - area of parallelogram

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

sock, address = conn.accept()
sock.send("Input length of base of parallelogram:".encode())
b = int(sock.recv(16384).decode())  # Base length
sock.send("Input height of parallelogram:".encode())
h = int(sock.recv(16384).decode())  # Height
area = b * h
sock.send(f"Area of parallelogram is:\n{b} x {h} = {area}".encode())
conn.close()
