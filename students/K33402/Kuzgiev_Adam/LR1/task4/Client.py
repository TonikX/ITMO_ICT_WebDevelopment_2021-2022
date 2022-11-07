import socket
import threading


HOST, PORT = "127.0.0.1", 14900

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))

name = input("Please enter ur name: ")

def listen():
    while True:
        msg = conn.recv(16384).decode()
        if msg == "name":
            conn.send(name.encode)
        else:
            print(msg)
    return

def send():
    while True:
        msg = f"\n>>> Пользователь {name}: \n{input('')}\n".encode("utf-8")
        conn.send(msg)
    return



listen_thread = threading.Thread(target=listen)
listen_thread.start()
send_thread = threading.Thread(target=send)
send_thread.start()