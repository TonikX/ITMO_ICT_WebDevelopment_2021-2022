import threading
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9099

server = '127.0.0.1', 9099
sock.connect(server)

self_name = input('Enter your nickname: ')
sock.send(self_name.encode('utf-8'))

def get_mes():
    while True:
        get_message = (sock.recv(1024)).decode('utf-8')
        print(get_message)

def send_mes():
    while True:
        message = input()
        sock.send(f'{self_name}: {message}'.encode('utf-8'))

t1 = threading.Thread(target=get_mes, name='input')
t1.start()
t2 = threading.Thread(target=send_mes, name='out')
t2.start()


