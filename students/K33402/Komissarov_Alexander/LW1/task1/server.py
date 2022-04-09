#server

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 10203))
sock.listen(1)


while True:
    clientsocket, address = sock.accept()
    print ('Incoming connection:', address)
    msg=clientsocket.recv(10203).decode('utf-8')
    print(msg)
    clientsocket.send(b'Hello, client! \n')
    clientsocket.close()
