import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))


def listen():
    while True:
        msg = conn.recv(16384)
        print(msg.decode("utf-8"))


def send():
    listen_thread = threading.Thread(target=listen)
    listen_thread.start()
    while True:
        conn.send(input(">> ").encode("utf-8"))

send()

