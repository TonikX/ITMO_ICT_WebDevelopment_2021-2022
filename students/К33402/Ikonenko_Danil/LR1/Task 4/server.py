import socket
import sys
from threading import Thread


class ChatServer:

    def __init__(self, host: str, port: int):
        self.clients = []
        self.host = host
        self.port = port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def shutdown(self):
        for sock in self.clients:
            sock.close()
        self.conn.close()
        sys.exit(0)

    def client_broadcast(self, message: bytes, sender: socket.socket) -> None:
        for sock in self.clients.copy():
            if sock != sender:
                try:
                    sock.send(message)
                except OSError:
                    print("Someone disconnected")
                    self.clients.remove(sock)

    def client_listen(self, sock: socket.socket) -> None:
        sock.settimeout(30)
        while True:
            try:
                message = sock.recv(1024)
                print(message.decode())
                self.client_broadcast(message, sock)
            except OSError:
                sock.close()
                break

    def main(self) -> None:
        self.conn.bind((self.host, self.port))
        self.conn.listen(10)
        while True:
            try:
                sock, address = self.conn.accept()
                print(f"Connection at {address}")
                self.clients.append(sock)
                Thread(target=self.client_listen, args=(sock,)).start()
            except KeyboardInterrupt:
                self.shutdown()

    def run(self) -> None:
        Thread(target=self.main).start()


if __name__ == '__main__':
    print("Starting server...")
    server = ChatServer('127.0.0.1', 3228)
    server.run()
    print("Server started")
