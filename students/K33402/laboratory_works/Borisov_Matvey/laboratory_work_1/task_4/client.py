from socket import *
import threading


def read():
    while True:
        data = connection.recv(16384)
        print(data.decode("utf-8"))


def chat():
    name = input("Enter user name: ")
    connection.sendto((name + " connected").encode("utf-8"), server_address)
    while True:
        connection.sendto((name + ": " + input()).encode("utf-8"), server_address)


server_address = "127.0.0.1", 14900
connection = socket(AF_INET, SOCK_DGRAM)
thread1, thread2 = threading.Thread(target=read), threading.Thread(target=chat)
thread1.start(), thread2.start()
