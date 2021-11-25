import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 5000))


def accept_from_server():
    while True:
        data = conn.recv(16384)
        print(data.decode("utf-8"))

accept_thread = threading.Thread(target=accept_from_server)
accept_thread.start()
while True:
    conn.send(input().encode())
