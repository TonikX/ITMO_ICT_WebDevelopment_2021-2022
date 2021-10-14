import socket
import threading

username = input("your username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5002))


def receive():
    while True:
        try:
            message = client.recv(4096).decode('utf-8')
            if message == 'NICKNAME':
                client.send(username.encode('utf-8'))
            else:
                print(message)

        except Exception as e:
            print(e)
            client.close()
            break


def send():
    while True:
        message = input()
        client.send(f'{username} > {message}'.encode('utf-8'))


send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=receive)
send_thread.start()
recv_thread.start()
