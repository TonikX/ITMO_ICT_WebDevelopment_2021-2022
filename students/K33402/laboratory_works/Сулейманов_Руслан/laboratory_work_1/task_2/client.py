import socket
import pickle

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Поиск площади трапеции.')
obj = {
    'a': input('Введите первое оснвоание a: '),
    'b': input('Введите второе оснвоание b: '),
    'h': input('Введите расстояние между основаниями - высоту h: ')
}
data = pickle.dumps(obj)
if data:
    sock.send(data)

data = sock.recv(4096)
sock.close()
udata = data.decode("utf-8")
print(udata)



