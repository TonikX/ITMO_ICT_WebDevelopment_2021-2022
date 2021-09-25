import socket
import sys
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 3346))

sockets_list = [sys.stdin, client]

def send_message():
    client.send(message.encode("utf-8"))
def read_message():
    while True:
        message = client.recv(1024)
        print(message.decode("utf-8"))

while True:
    try:
        message = input('Как тебя зовут? - ')
        stream_send = threading.Thread(target=send_message)
        stream_read = threading.Thread(target=read_message)
        stream_read.start()
        stream_send.start()

    except KeyboardInterrupt:
        client.close()