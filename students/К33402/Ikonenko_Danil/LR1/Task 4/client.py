import socket
import sys
from threading import Thread


class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self):
        while True:
            try:
                msg = input()
                self.conn.send(f"{self.username}: {msg}".encode())
            except (KeyboardInterrupt, EOFError):
                self.conn.close()
                sys.exit(0)

    def recieve(self):
        while True:
            try:
                print(self.conn.recv(1024).decode())
            except KeyboardInterrupt:
                self.conn.close()
                sys.exit(0)
            except ConnectionError:
                # Unexpected connection error
                print("Connection error")
                self.conn.close()
                sys.exit(1)

    def run(self):
        self.conn.connect((self.host, self.port))
        # Run threaded functions
        Thread(target=self.send).start()
        Thread(target=self.recieve).start()


if __name__ == '__main__':
    u = input("Your username: ")
    print(f"Hello {u}")
    print("Connecting to server...")
    client = ChatClient('127.0.0.1', 3228, u)
    client.run()
