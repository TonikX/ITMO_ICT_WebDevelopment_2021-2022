import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9099

clients = list()

sock.bind((host, port))
sock.listen(10)

def chatting(conn):
    while True:
        message = (conn.recv(1024))
        send_to_all(conn, message)

def send_to_all(conn, message):
    for client in clients:
        if conn != client:
            client.send(message)

def new_client():
    while True:
        conn, addr = sock.accept()
        clients.append(conn)
        client_name = (conn.recv(1024)).decode('utf-8')
        mes = f'{client_name} has joined.'
        send_to_all(conn, mes.encode('utf-8'))
        index = threading.Thread(target=chatting, args=(conn,))
        index.start()


t1 = threading.Thread(target=new_client, name='input')
t1.start()

