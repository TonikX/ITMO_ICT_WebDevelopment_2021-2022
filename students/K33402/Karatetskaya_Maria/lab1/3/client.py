import socket
import time
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("localhost", 8080))
a = int(input('Введите количесво дисциплин\n'))
list = ''
for i in range(a):
    list += (input('Введите ' + str(i+1) + ' дисциплину и количество баллов \n')) +' '
conn.send(list.encode('utf-8'))
data = conn.recv(22222)
udata = data.decode()
print(udata)
data = conn.recv(22222)
udata = data.decode()
print(udata)
time.sleep(15)
conn.close