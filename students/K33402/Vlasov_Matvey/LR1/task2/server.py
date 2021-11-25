import socket

conn = socket.socket()
conn.bind(("127.0.0.1", 2334))
conn.listen(5)

while True:
    try:
        client, (client_host, client_port) = conn.accept()
        data = client.recv(1024).decode("utf-8")
        a, b, c = map(lambda x: int(x), data.split())
        if a == 0:
            raise ValueError("This equation is not quadratic!")

        d = b ** 2 - 4 * a * c
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        answer = "The roots of the quadratic equation are {:.2f} and {:.2f}".format(x1, x2).encode("utf-8")
        client.send(answer)
    except KeyboardInterrupt:
        conn.close()
