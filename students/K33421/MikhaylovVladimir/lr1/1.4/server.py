import socket
from threading import Thread
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(10)
sock.setblocking(False)

clients = []


def get_users():
    while True:
        sock.setblocking(True)
        clientsocket, addr = sock.accept()
        sock.setblocking(False)
        if clientsocket not in clients:
            clients.append((clientsocket, addr))
            print('New client appeared: ', addr)


def message():
    while True:
        text = None
        for user in clients:
            text = user[0].recv(1024).decode('utf-8')
            print('Received text: ' + text)
            if text == "quit":
                user[0].close()
                print('User have left the chat: ', user[1])
                text = f'User {user[1]} have left the chat'
            for send_user in clients:
                if send_user[0] == user[0]:
                    continue
                data = f'User {user[1]}: ' + text
                send_user[0].sendall(data.encode('utf8'))


user_thread = Thread(target=get_users)
chat_thread = Thread(target=message)

user_thread.start()
chat_thread.start()