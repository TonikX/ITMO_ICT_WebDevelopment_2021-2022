import socket
from threading import Thread
import threading


class Server:

    def __init__(self):
        sock.bind(('localhost', 9090))
        sock.listen(10)
        print("Server was started on socket:", sock)
        print("Wait for users...")

    def get_socket(self):
        while True:
            client, addr = sock.accept()
            clients.append({"connection": client, "socket": addr})
            print("connected:", addr)
            Thread(target=self.check_messages, args=(client,)).start()

    def check_messages(self, client):
        while True:
            try:
                data = client.recv(4096)
                message = str(data.decode("utf-8"))
                self.broadcast(client, message)
            except Exception as ex:
                self.delete_user_socket(client)
                break

    def delete_user_socket(self, client):
        for user in clients:
            if user["connection"] == client:
                clients.remove(user)
                break

    def broadcast(self, client, message: str):
        message += "\n"
        for user in clients:
            if user["connection"] != client:
                user["connection"].send(message.encode())


if __name__ == "__main__":
    sock = socket.socket()
    clients = []
    server = Server()
    thread = threading.Thread(target=server.get_socket())
    thread.start()
    thread.join()