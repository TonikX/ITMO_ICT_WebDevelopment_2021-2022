import socket 

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('Hello, server'.encode()) # Отпрвка сообщения на сервер, encode() превращает текст в байты

data = sock.recv(1024)
print(data)

sock.close() # закрыть подключение 