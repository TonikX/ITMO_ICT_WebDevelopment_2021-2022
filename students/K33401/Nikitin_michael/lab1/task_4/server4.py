import socket
from threading import Thread


sock = socket.socket()
sock.bind(('127.0.0.1', 53331))
sock.listen(10)
users = []


def adder():
    while True:
        global users
        users.append(sock.accept()[0])
        print("Пользователь подключился, стало:", len(users))


def users_counter():
    while True:
        for i in range(len(users)):
            try:
                data = users[i].recv(4096)
                if data:
                    message = data.decode()
                    print(message)
                    if message == "exit":
                        users.pop(i)
                        print("Пользователь отключился, осталось:", len(users))
            except socket.error as error:
                if error.errno == 10054:
                    users.pop(i)
                    print("Пользователь отключился, осталось:", len(users))
                else:
                    raise


def messenger():
    while True:
        global users
        message = input()
        if message:
            for i in range(len(users)):
                users[i].send(message.encode())


user_thread = Thread(target=users_counter)
message_thread = Thread(target=messenger)
adder_thread = Thread(target=adder)


user_thread.start()
message_thread.start()
adder_thread.start()

