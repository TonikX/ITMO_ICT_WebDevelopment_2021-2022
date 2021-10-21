import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8000))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384).decode("utf-8")
        print("data: ", data)
        clientsocket.send(b"Hello, client! \n")
    except KeyboardInterrupt:
        conn.close()
        break