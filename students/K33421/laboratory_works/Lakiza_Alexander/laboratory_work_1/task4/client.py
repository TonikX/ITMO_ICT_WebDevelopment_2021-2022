import socket
import threading

address = "127.0.0.1", 53210
conn = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
conn.connect(('127.0.0.1', 53210))


def messages():
    while True:
        data = conn.recv(2048)
        print(data.decode("utf-8"))


def chat():
    name = input("Enter your name: ")
    print(f'{name}, say hello to the chat')
    conn.sendall(bytes(f"{name} joined", "utf-8"))
    while True:
        conn.sendto(bytes(f"{name}: {input()}", "utf-8"), address)


if __name__ == "__main__":
    thread1, thread2 = threading.Thread(target=messages), threading.Thread(target=chat)
    thread1.start(), thread2.start()
