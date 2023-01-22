import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'

name = input('Введите свой ник\n')
port = 9090
client.connect((host, port))
print(name + ' ' + 'подключился к серверу\n')

def send_mes():
    while True:
        outdata = input('')
        print()
        client.send(f'{name}:{outdata}'.encode('utf-8'))
        print('%s:%s' % (name, outdata))

def get_mes():
    while True:
        indata = client.recv(1024)
        print(indata.decode('utf-8'))

t1 = threading.Thread(target=get_mes, name='input')
t2 = threading.Thread(target=send_mes, name='out')
t1.start()
t2.start()
t2.join()
print('сервер отключен')
client.close()
