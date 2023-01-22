import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 9090
server.bind((host, port))

server.listen(5)

clients = list()
end = list()
def get():
    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f'сервер подключен через {addr}: количество клиентов:  {len (clients)}', end = '\n')

def recv_data(client):
    while True:
        try:
            indata = client.recv(1024)
        except Exception:
            clients.remove(client)
            end.remove(client)
            print( f'Сервер отключен: количество клиентов: {len (clients)}', end = '\n')
            break
        print(indata.decode('utf-8'))
        for i in clients:
            if i != client:
                i.send(indata)

def send_mes():
    while True:
        print('')
        outdata = input('')
        print()
    for client in clients:
        client.send(f"Сервер: {outdata}".encode('utf-8)'))

def get_mes():
    while True:
        for i in clients:
            if i in end:
                continue
            index = threading.Thread(target=recv_data, args=(i,))
            index.start()
            end.append(i)

t1 = threading.Thread(target=send_mes, name='input')
t1.start()
t2 = threading.Thread(target=get_mes, name='out')
t2.start()
t3 = threading.Thread(target=get(), name='get')
t3.start()
t2.join()

for i in clients:
    i.close()