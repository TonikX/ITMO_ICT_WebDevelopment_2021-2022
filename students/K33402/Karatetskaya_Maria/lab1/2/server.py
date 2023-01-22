import socket
import time
import math
def pif(a,b):
    return str(math.sqrt(a*a + b*b))

def equation(a,b, c):
    d = b*b - 4*a*c
    if d == 0:
        return 'корень '+ str((math.sqrt(d) - b)/2/a)
    elif d > 0:
        x1 = (math.sqrt(d) - b)/2/a
        x2 = -1*(math.sqrt(d) + b)/2/a
        return str('1 корень '+str(x1)+'\n2 корень '+str(x2))
    else:
        return 'нет корней'
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 1234))
conn.listen(1)

clientsocket, address = conn.accept()
data = clientsocket.recv(22222)
if data:
    udata = data.decode("utf-8")
    if udata == '1':
        clientsocket.send(str.encode("Введите перый катет \n"))
        data = clientsocket.recv(22222)
        a = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode("Введите второй катет \n"))
        data = clientsocket.recv(22222)
        b = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode(pif(a,b)))

    if udata == '2':
        clientsocket.send(str.encode("Введите перый член квадратного уравнения \n"))
        data = clientsocket.recv(22222)
        a = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode("Введите второй член квадратного уравнения \n"))
        data = clientsocket.recv(22222)
        b = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode("Введите третий член квадратного уравнения \n"))
        data = clientsocket.recv(22222)
        c = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode(equation(a,b, c)))

    if udata == '3':
        clientsocket.send(str.encode("Введите первую сторону трапеции \n"))
        data = clientsocket.recv(22222)
        a = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode("Введите вторуую сторону трапеции  \n"))
        data = clientsocket.recv(22222)
        b = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode("Введите высоту трапеции \n"))
        data = clientsocket.recv(22222)
        c = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode(str((a+b)*c/2)))

    if udata == '4':
        clientsocket.send(str.encode("Введите сторону параллелограмма \n"))
        data = clientsocket.recv(22222)
        a = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode("Введите высоту параллелограмма  \n"))
        data = clientsocket.recv(22222)
        b = int(data.decode("utf-8"))
        clientsocket.sendall(str.encode(str(a*b)))

conn.close()


