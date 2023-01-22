import socket
import time
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 1234))       #открытие сокета
conn.send(b"Hello, server! \n")         #отправка приветствия сереру
print('message send \n')
time.sleep(3)
data = conn.recv(22222)
udata = data.decode("utf-8")
print(udata)
conn.close