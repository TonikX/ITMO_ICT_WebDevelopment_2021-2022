import argparse
import os
import socket
import threading
import time

parser = argparse.ArgumentParser(description='Сервер для задачи №4')
parser.add_argument('--host', help='IP хоста', default='localhost')
parser.add_argument('--port', help='Порт хоста', default=8888)
parser.add_argument('--uname', help='Имя пользователя', default='')

args = parser.parse_args()

if args.uname == '':
    username = input('Введите имя пользователя: ')
else:
    username = args.uname

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((args.host, args.port))

hello_server = f"= {username} = Присоединился к серверу!"
conn.send(hello_server.encode("utf-8"))

messages = []


def receive_message():
    global messages

    while True:
        message = conn.recv(2000).decode()
        messages.append(message)

        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n'.join(messages), end='', flush=True)


def send_message():
    while True:
        inpmsg = '\nВведите сообщение: '
        conn.send(f' - {username} - {input(inpmsg)}'.encode())


threading.Thread(target=receive_message).start()
threading.Thread(target=send_message).start()
