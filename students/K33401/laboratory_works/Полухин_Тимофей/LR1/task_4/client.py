import os
import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(('127.0.0.1', 8080))

messages = []


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def receive_message():
    while True:
        message = conn.recv(2000).decode()
        messages.append(message)

        clear_console()
        print('\n\n'.join(messages), end='')
        print('\n\nYou: ', end='')


def send_message():
    while True:
        conn.send(input().encode())


clear_console()
print('Enter username: ', end='')

threading.Thread(target=receive_message).start()
threading.Thread(target=send_message).start()
