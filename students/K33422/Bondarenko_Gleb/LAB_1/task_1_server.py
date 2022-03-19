import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384)
        udata = data.decode("utf-8")
        print("data: ", udata)
        clientsocket.send(b"Hello, my dear client! \n")
    except KeyboardInterrupt:
        conn.close()
        break

        a, b, h = map(lambda x: int(x), data.split())
