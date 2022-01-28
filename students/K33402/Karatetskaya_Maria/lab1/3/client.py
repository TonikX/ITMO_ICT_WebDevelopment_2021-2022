import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

GET_request = ["GET isu.ifmo.ru/pls/apex/f HTTP/1.1",
        "Host: example.local",
        "Accept: text/html",
        "User-Agent: Mozilla/5.0"]

POST_request = ["POST isu.ifmo.ru/pls/apex/f?Petrov=74 HTTP/1.1",
        "Host: example.local",
        "Accept: text/html",
        "User-Agent: Mozilla/5.0"]

sock.send("\r\n".join(POST_request).encode())

print("Ждем ответ от сервера...")
data = sock.recv(1024)
sock.close()

print(data.decode())