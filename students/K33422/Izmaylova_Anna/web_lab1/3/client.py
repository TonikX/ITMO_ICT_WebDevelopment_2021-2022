import socket 

sock = socket.socket()
port = int(input("Введите порт: "))
sock.connect(('localhost', port))

choose = input("Посмотреть оценки - get\nЗаписать новую оценку в файл - post\n")

if choose == "get":
    req = f"GET isu.ifmo.ru/pls/apex/f HTTP/1.1\r\n" 
elif choose == "post":
    name = input("Введите имя: ")
    grade = input("Введите оценку: ")
    req = f"POST isu.ifmo.ru/pls/apex/f?name={name}&grade={grade} HTTP/1.1\r\n" 

sock.send(req.encode()) # Отправка сообщения на сервер, encode() превращает текст в байты

data = sock.recv(1024)
print(data)

sock.close() # закрыть подключение 