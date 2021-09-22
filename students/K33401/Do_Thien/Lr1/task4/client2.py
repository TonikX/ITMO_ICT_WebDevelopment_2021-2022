import socket
import threading

PORT = 7000
HOST = '127.0.0.1'
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((HOST, PORT))

name = input("Choose your name: ")

def receive():
    while True:
        try:
            message = clientSock.recv(1024).decode('utf-8')
            if message == "NAME":
                clientSock.send(name.encode('utf-8'))
            else:
                print(message)
        except socket.error as e:
            print(str(e))
            break

def write_mess():
    while True:
        message = "{} : {}".format(name, input())
        clientSock.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write_mess)
write_thread.start()

