import socket
import threading

s = socket.socket()
host = "127.0.0.1"
port = 5556
s.connect((host, port))
user = input("Your username? ")

def recieving_message():
    while True:
        message = s.recv(16384).decode("utf-8")
        if message == "username?":
            s.send(user.encode("utf-8"))
        else:
            print(message)

def sending_message():
    while True:
        text = input('')
        if text == 'close':
            s.send(text.encode("utf-8"))
            s.close()
            break
        else:
            message = '{}: {}'.format(user, text)
            s.send(message.encode("utf-8"))

recieve_thread = threading.Thread(target=recieving_message)
recieve_thread.start()
sending_thread = threading.Thread(target=sending_message)
sending_thread.start()