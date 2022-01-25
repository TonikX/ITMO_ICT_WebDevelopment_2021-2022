import socket, threading # потоки

sock = socket.socket()
port = int(input("Введите порт: "))
sock.connect(('localhost', port))

name = input("Введите ваш ник: ")
sock.send(name.encode())

def listen_server():
    while True:
        data = sock.recv(1024)
        print(data.decode())

def send_to_server():
    listen_tread = threading.Thread(target=listen_server)
    listen_tread.start() # запустили паралелльную работу функции listen_server

    while True:
        message = input()
        sock.send(message.encode())

send_to_server()

sock.close() # закрыть подключение 