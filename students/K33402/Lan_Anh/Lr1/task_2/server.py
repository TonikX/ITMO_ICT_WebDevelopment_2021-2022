import socket
from threading import Thread
import threading
import math


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
                data = str(data.decode("utf-8"))
                if not data == "Square Equations":
                    self.target_cast(client, "Такой задачи нет(")
                    continue
                self.target_cast(client, "Введите a, b, c через пробел")
                data = client.recv(4096)
                data = str(data.decode("utf-8"))
                a, b, c = map(float, [i.strip() for i in data.split()])
                discr = b ** 2 - 4 * a * c
                if discr > 0:
                    x1 = (-b + math.sqrt(discr)) / (2 * a)
                    x2 = (-b - math.sqrt(discr)) / (2 * a)
                    self.target_cast(client, "x1 = %.2f \nx2 = %.2f" % (x1, x2))
                elif discr == 0:
                    x = -b / (2 * a)
                    self.target_cast(client, "x = %.2f" % x)
                else:
                    self.target_cast(client, "Корней нет")
            except Exception as ex:
                print(ex)
                self.delete_user_socket(client)
                break

    def delete_user_socket(self, client):
        print("delete user", client)
        for user in clients:
            if user["connection"] == client:
                clients.remove(user)
                break

    def target_cast(self, client, message):
        message += "\n"
        client.send(message.encode())


if __name__ == "__main__":
    sock = socket.socket()
    clients = []
    server = Server()
    thread = threading.Thread(target=server.get_socket())
    thread.start()
    thread.join()