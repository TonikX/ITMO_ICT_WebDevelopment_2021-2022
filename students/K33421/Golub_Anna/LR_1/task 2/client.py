import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9000))

# sending message to server
a = input('Верхнее основание трапеции: ')
b = input('Нижнее основание трапеции: ')
h = input('Высота трапеции: ')
message = ' '.join([str(a), str(b), str(h)]).encode()
conn.send(message)

# receiving server's response
data = conn.recv(16384)
data = data.decode('utf-8')
print('Площадь трапеции равна', data)

conn.close()
