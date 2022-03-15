import argparse
import socket
from threading import *


class ChatThread(Thread):
    def __init__(self, conn, sender):
        self.conn = conn
        self.sender = sender

        super().__init__()

    def run(self):
        while True:
            try:
                message = self.conn.recv(1024)
                message = self.sender + ': ' + message.decode()
                send_for_all(message, self.sender)
            except:
                self.conn.close()


def send_for_all(message, sender):
    for client in clients:
        if client.sender != sender:
            try:
                client.conn.send(message.encode())
            except:
                client.conn.close()
                clients.remove(client)


parser = argparse.ArgumentParser(description='Сервер для задачи №4')
parser.add_argument('--host', help='IP хоста', default='localhost')
parser.add_argument('--port', help='Порт хоста', default=8888)

args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((args.host, args.port))
    sock.listen()

    print(f'Сервер запущен по адресу {args.host}:{args.port}')

    clients = []
    while True:
        try:
            conn, addr = sock.accept()
            client_host, client_port = addr

            new_chat = ChatThread(conn, str(client_port))
            clients.append(new_chat)
            new_chat.start()

        except KeyboardInterrupt:
            sock.close()
            for client in clients:
                client.conn.close()
