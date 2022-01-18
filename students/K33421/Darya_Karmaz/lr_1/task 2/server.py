import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8001))
conn.listen(10)

while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384)
        data = data.decode("utf-8")
        data = data.split()
        a, h = float(data[0]), float(data[1])
        s = str(a * h).encode()
        clientsocket.send(s)
    except KeyboardInterrupt:
        conn.close()
        break
