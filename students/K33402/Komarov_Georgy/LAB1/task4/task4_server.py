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
                message = self.conn.recv(args.buffer)
                message = self.sender + ': ' + message.decode()
                broadcast(message, self.sender)
            except:
                self.conn.close()


def broadcast(message, sender):
    for client in clients:
        if client.sender != sender:
            try:
                client.conn.send(message.encode())
            except:
                client.conn.close()
                clients.remove(client)


parser = argparse.ArgumentParser(description='Task 4 Server')
parser.add_argument('--host', help='Hostname/IP to bind', default='127.0.0.1')
parser.add_argument('--port', help='Port to bind', default=1337)
parser.add_argument('-b', '--buffer', help='Connection buffer size', type=int, default=1024)
args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((args.host, args.port))
    sock.listen()

    clients = []
    while True:
        try:
            conn, addr = sock.accept()
            client_host, client_port = addr

            new_thread = ChatThread(conn, str(client_port))
            clients.append(new_thread)
            new_thread.start()

        except KeyboardInterrupt:
            sock.close()
            for client in clients:
                client.conn.close()
