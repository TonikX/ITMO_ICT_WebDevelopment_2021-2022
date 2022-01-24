import socket
from threading import Thread
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7774))
sock.listen(10)
sock.setblocking(False)
users = []


def new_users():
    while True:
        sock.setblocking(True)
        clientsocket, addr = sock.accept()
        sock.setblocking(False)
        if clientsocket not in users:
            users.append((clientsocket, addr))
            print('New user:', addr)


def chat():
    while True:
        try:
            for user in users:
                message = user[0].recv(1024).decode('utf-8')
                print(user[-1], '`s message: ' + message)
            for send_user in users:
                    if send_user[0] == user[0]:
                        continue
                    data = f'User {user[1]}: ' + message
                    send_user[0].send(data.encode('utf8'))
        except socket.error:
            time.sleep(5)
        except KeyboardInterrupt:
            for user in users:
                user[0].close()
            break


user_thread = Thread(target=new_users)
chat_thread = Thread(target=chat)

user_thread.start()
chat_thread.start()

