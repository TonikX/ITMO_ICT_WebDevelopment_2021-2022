import socket
import threading
import datetime

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1', 8000))

username = input('Придумайте имя пользователя: ')


def receiver():
    while True:
        print(conn.recv(1024).decode())


def sender():
    while True:
        msg = f'[{datetime.datetime.now().strftime("%H:%M:%S")}] {username}: {input()}'
        conn.send(msg.encode())


recv_thr = threading.Thread(target=receiver).start()
print_thr = threading.Thread(target=sender).start()
