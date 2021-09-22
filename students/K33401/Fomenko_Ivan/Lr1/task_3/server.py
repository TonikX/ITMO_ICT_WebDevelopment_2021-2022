import socket
import mimetypes

class Server:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(10)

    def load_html(self, path: str):
        clientsocket, address = self.sock.accept()
        content = b""
        with open(path, "rb") as f:
            content = f.read()
        content_type, _ = mimetypes.guess_type(path) # In case of future modifications
        status = 200 # Same here
        status_string = "OK" # Here
        headers = f"Content-Type: {content_type}\n" # And here
        http1 = f"HTTP/1.0 {status} {status_string}\n" + headers
        response = http1.encode() + content
        clientsocket.send(response)
        clientsocket.close()

    def die(self):
        self.sock.close()


if __name__ == '__main__':
    host = "localhost"
    port = 14900
    server = Server(host, port)
    path = "index.html"
    while True:
        try:
            server.load_html(path)
        except KeyboardInterrupt:
            server.die()
            break