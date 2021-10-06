import socket
import time
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 1234))
conn.listen(10)

clientsocket, address = conn.accept()
data = clientsocket.recv(22222)
if data:
    udata = data.decode("utf-8")
    print(udata)
    time.sleep(3)
    clientsocket.sendall(b"Hello, client! \n")
    print('message send')
conn.close()
