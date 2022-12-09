import socket

conn = socket.socket()

conn.connect(('127.0.0.1', 7896))

conn.send(input("Введите а: ").encode())
conn.send(input("Введите b: ").encode())
conn.send(input("Введите c: ").encode())

print("Решение: ", conn.recv(16384).decode('utf-8'))

conn.close()
