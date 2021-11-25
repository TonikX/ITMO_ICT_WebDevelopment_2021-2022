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
        print(data)

        # sending a response
        client_socket.send(b'Hello client! \n')

    except KeyboardInterrupt:
        conn.close()
        break
