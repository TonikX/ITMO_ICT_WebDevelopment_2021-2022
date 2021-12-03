import socket # библиотека для приема/передачи данных
import threading # имортируем потоки

sock = socket.socket() # создание сокета (комбинация IP и номера порта)
port = int(input("Введите порт: "))
sock.bind(('127.0.0.1', port)) 
sock.listen(3) # сколько клиентов готов слушать сервер

clients = [] # список с подключениями клиентов
names = []

def send_to_clients(name, data):
    for i in range(len(names)):
        if names[i] != name: # если какое-то имя из списка не является именем отправителя
            clients[i].send(f"({name}): ".encode() + data) # (Dasha): Hey
            

def listen_client(socket):
    while True:
        data = socket.recv(1024)

        pos = clients.index(socket) 
        name = names[pos] 
        send_to_clients(name, data)


def server_accept():
    while True:
        conn, addr = sock.accept()

        # получим имя клиента 
        data = conn.recv(1024)
        name = data.decode()
        names.append(name)

        print(f"Client {name} accepted")

        clients.append(conn)
        listen_tread = threading.Thread(target=listen_client, args=(conn,))
        listen_tread.start()


server_accept()