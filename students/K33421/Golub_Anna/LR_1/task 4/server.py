import socket
from threading import *


class ChatThread(Thread):
    def __init__(self, conn, client_name):
        Thread.__init__(self)
        self.conn = conn
        self.client_name = client_name

    def run(self):
        while True:
            try:
                message = self.conn.recv(1024)
                message = self.client_name + ': ' + message.decode()
                print(message)
                broadcast(message, self.client_name)
            except:
                self.conn.close()


def broadcast(message, author):
    for client in client_list:
        if client.client_name != author:
            try:
                client.conn.send(message.encode())
            except:
                client.conn.close()
                client_list.remove(client)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 9000))
server.listen(10)

client_list = []
while True:
    try:
        conn, addr = server.accept()
        print(addr, 'connected')

        new_thread = ChatThread(conn, str(addr[1]))
        client_list.append(new_thread)
        new_thread.start()

    except KeyboardInterrupt:
        server.close()
        for client in client_list:
            client.conn.close()
