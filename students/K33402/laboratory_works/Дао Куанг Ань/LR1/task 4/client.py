import threading
import socket


client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cname = input('Choose a name:')
host = '127.0.0.1'
port = 555
client.connect((host, port))


def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "cname":
                client.send(cname.encode("utf-8"))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        message = f'{cname}: {input("")}'
        client.send(message.encode("utf-8"))



receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()