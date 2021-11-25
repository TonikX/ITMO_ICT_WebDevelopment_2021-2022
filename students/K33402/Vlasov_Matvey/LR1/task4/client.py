import socket
import threading

conn = socket.socket()
conn.connect(("127.0.0.1", 2334))

name = input("Enter your name: ")
conn.send(f"{name} joined the chat".encode("utf-8"))


def chat():
    while True:
        msg = input()
        conn.send(f"{name}: {msg}".encode("utf-8"))


def read():
    while True:
        data = conn.recv(1024).decode("utf-8")
        if data:
            print(data)


chat_thread = threading.Thread(target=chat)
read_thread = threading.Thread(target=read)
chat_thread.start()
read_thread.start()
