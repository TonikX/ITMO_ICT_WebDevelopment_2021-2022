import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 9000))
conn.listen(1)

while True:
    try:
        client_socket, address = conn.accept()
        with open('index.html', 'r') as index_file:
            message = index_file.read()
        client_socket.send(b'HTTP/1.1 200 OK\n' + b'Content-Type: text/html\n' +
                           b'\n' + message.encode())
    except KeyboardInterrupt:
        conn.close()
        break
