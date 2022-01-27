import socket
import math

sock = socket.socket()
sock.bind(("127.0.0.1", 5667))
sock.listen(1)

while True:
    try:
        conn, address = sock.accept()
        data = conn.recv(12446)
        a, b = data.decode("utf-8").split(",")
        answer = str(math.sqrt(int(a)**2 + int(b)**2))
        conn.send(answer.encode("utf-8"))
        conn.close
    except KeyboardInterrupt:
        sock.close()
        break