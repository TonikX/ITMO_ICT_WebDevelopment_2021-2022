import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 9000))
conn.listen(10)

while True:
    try:
        # receiving client's message
        client_socket, address = conn.accept()
        data = client_socket.recv(16384)
        data = data.decode('utf-8')
        a, b, h = map(int, data.lstrip().rstrip().split())
        print('a =', a)
        print('b =', b)
        print('h =', h)

        # sending a response
        s = 0.5 * (a + b) * h
        s = str(s).encode()
        client_socket.send(s)

    except KeyboardInterrupt:
        conn.close()
        break
