import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 14900))
conn.listen(10)


def main():
    while True:
        try:
            client, _ = conn.accept()
            client.recv(4096)
            # Set appropriate headers
            response_type = "HTTP/1.0 200 OK\n"
            headers = "Content-Type: text/html\n\n"
            # Read HTML from file
            with open("index.html", "r") as f:
                body = f.read()
            resp = response_type + headers + body
            client.send(resp.encode())
            client.close()
        except KeyboardInterrupt:
            conn.close()
            break


if __name__ == '__main__':
    main()
