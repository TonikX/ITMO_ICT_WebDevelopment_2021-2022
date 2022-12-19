import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 2235))

nickname = input('Enter your nickname: ')


def listen_server():
    while True:
        msg = s.recv(2048).decode()
        if msg == 'nickname':
           s.send(nickname.encode())
        else:
            print(msg)

def send_data():
    while True:
        msg = f"\n>>> Пользователь {nickname}: \n{input('')}\n".encode("utf-8")
        s.send(msg)

listen_thread = threading.Thread(target=listen_server)
listen_thread.start()
send_thread = threading.Thread(target=send_data)
send_thread.start()
    