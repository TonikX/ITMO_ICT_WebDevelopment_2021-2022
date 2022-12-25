import socket, threading

client = socket.socket()
client.connect(('localhost', 9090))

name = input("Input your name, please: ")
client.send(name.encode())

def listen_server():
    while True:
        data = client.recv(1024)
        print(data.decode())

def send_to_server():
    listen_thread = threading.Thread(target=listen_server)
    listen_thread.start()

    while True:
        client.send(input().encode())    

send_to_server()