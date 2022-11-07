#server

import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 10203))
sock.listen(1)


while True:
    clientsocket, address = sock.accept()
    print ('Incoming connection:', address)
    msg=clientsocket.recv(10203).decode('utf-8')
    a, b = msg.split()
    a, b = int(a), int(b)
    c = str(math.sqrt(a*a+b*b))
    print(c)
    sending="Длина гипотенузы равна: "+c
    clientsocket.send(str(sending).encode())
    clientsocket.close()
