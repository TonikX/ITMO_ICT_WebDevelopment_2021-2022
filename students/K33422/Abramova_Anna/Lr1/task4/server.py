import socket
from threading import Thread


class Chat:
    def __init__(self, host, port):
        self.clients = {}
        self.host = host
        self.port = port
        self.chat_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.chat_sock.bind((host, port))
        self.chat_sock.listen()

        self.chat_loop()

    def chat_loop(self):
        while True:
            client_sock, _ = self.chat_sock.accept()
            name = client_sock.recv(1024)
            name = name.decode()
            self.clients[client_sock] = name

            client_thread = Thread(target=self.listen_client, args=(client_sock,))
            client_thread.start()

    def listen_client(self, sock):
        while True:
            data = sock.recv(1024)
            self.send_message_for_all(self.clients[sock], data)

    def send_message_for_all(self, client_name, message):
        for sock in self.clients:
            if self.clients[sock] != client_name:
                sock.send((client_name + ': ' + message.decode('utf-8')).encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000

    chat = Chat(host, port)

