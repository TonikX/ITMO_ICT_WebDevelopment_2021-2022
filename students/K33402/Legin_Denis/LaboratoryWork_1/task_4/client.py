import socket
import threading


def send_message():
    while True:
        text = input(" ")
        sock.sendall(text.encode('UTF-8'))
        if text == "q":
            sock.close()
            break


def receive_message():
    try:
        while True:
            data = sock.recv(1024)
            udata = data.decode("utf-8")
            print(udata)
    except ConnectionAbortedError:
        print('You left the chat')



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55551))

get_thread = threading.Thread(target=receive_message)
send_thread = threading.Thread(target=send_message)
get_thread.start(), send_thread.start()
