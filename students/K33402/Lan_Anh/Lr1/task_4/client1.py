
import socket
import threading

encoding = "UTF-8"
user_name = "user1"


def get_message():
    try:
        while True:
            message = sock.recv(1024).decode(encoding)
            print(message)
    except ConnectionResetError:
        pass


def send_message():
    try:
        while True:
            message = (user_name + ": " + input()).encode(encoding)
            sock.send(message)
    except Exception:
        pass

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 9090))

    get_message_thread = threading.Thread(target=get_message)
    get_message_thread.start()

    send_message_thread = threading.Thread(target=send_message)
    send_message_thread.start()

    get_message_thread.join()
    send_message_thread.join()

    sock.close()