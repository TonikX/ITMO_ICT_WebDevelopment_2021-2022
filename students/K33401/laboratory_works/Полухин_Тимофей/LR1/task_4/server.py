import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080

server.bind((host, port))
server.listen()

users = {}


def receive(current_conn):
    while True:
        message = current_conn.recv(2000).decode('utf-8')
        for conn in users:
            conn.send(f'{"You" if current_conn == conn else users[current_conn]}: {message}'.encode())


def run_server():
    while True:
        conn, addr = server.accept()

        username = conn.recv(2000).decode()
        users[conn] = username

        for conn in users:
            conn.send(f'{username} joined!'.encode())

        thread = threading.Thread(target=receive, args=(conn,))
        thread.start()


run_server()
