import socket
from threading import Thread


class ClientChat:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_sock = socket.socket()
        self.client_sock.connect((host, port))
        name = input("Enter your name: ")
        self.client_sock.send(name.encode())
        self.chat_loop()

    def listen_server(self):
        while True:
            data = self.client_sock.recv(1024)
            print(data.decode())

    def chat_loop(self):
        listen = Thread(target=self.listen_server)
        listen.start()

        while True:
            self.client_sock.send(input().encode())


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000

    chat = ClientChat(host, port)
