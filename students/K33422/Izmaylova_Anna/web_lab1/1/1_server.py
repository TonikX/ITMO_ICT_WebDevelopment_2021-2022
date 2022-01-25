import socket # библиотека для приема/передачи данных

sock = socket.socket() # создание сокета (комбинация IP и номера порта)
sock.bind(('127.0.0.1', 9090)) 
sock.listen(1) # сколько клиентов готов слушать сервер
connection, addr = sock.accept() # принимаем подключение

# print('connected:', addr)

data = connection.recv(1024) # Получение данных от клиента
connection.send("Hello, client".encode()) # Отправим ответ клиенту

print(data) 

connection.close() # Закроем подключение