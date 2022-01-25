import socket 

sock = socket.socket()
sock.connect(('localhost', 9091))
a = input("Введите a: ") 
b = input("Введите b: ") 
c = input("Введите c: ") 
req = f"GET https://localhost?a={a}&b={b}&c={c} HTTP/1.1" 

sock.send(req.encode()) # Отпрвка сообщения на сервер, encode() превращает текст в байты

data = sock.recv(1024)
print(data)

sock.close() # закрыть подключение 