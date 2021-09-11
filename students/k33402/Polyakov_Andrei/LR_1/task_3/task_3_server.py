import socket
import math

sock = socket.socket()
sock.bind(("127.0.0.1", 5667))
sock.listen(1)

while True:
    try:
        conn, address = sock.accept()
        with open("index.html", "r") as file:
            response_type = "HTTP/1.0 200 OK\n"
            headers = "content-type: text/html\n\n"
            body = file.read()
            response = response_type + headers + body
            conn.send(response.encode("utf-8"))
            conn.close
    except KeyboardInterrupt:
        sock.close()
        break