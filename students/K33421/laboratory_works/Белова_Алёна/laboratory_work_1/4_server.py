import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))
username = input("Enter your username: ")


def listen():
    while True:
        msg = conn.recv(16384)
        print(msg.decode("utf-8"))


def send():
    listen_thread = threading.Thread(target=listen)
    listen_thread.start()
    while True:
        text = input()
        conn.send((username + ": " + text).encode("utf-8"))

send()
