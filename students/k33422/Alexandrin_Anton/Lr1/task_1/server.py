import socket
import time


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 5000))
conn.listen(5)

while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(4096)
        udata = data.decode('utf-8')
        clientsocket.send(b'Hello, client')
        print(time.ctime() + '\n' + udata)

    except KeyboardInterrupt:
        conn.close()
        break
