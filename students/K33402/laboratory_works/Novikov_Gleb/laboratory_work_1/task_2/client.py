# Теорема Пифагора
import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 5000))
first_side = input("Enter the length of the first side: ")
second_side = input("Enter the length of the second side: ")
conn.send(first_side.encode())
conn.send(second_side.encode())
hypotenuse_bin = conn.recv(200)
hypotenuse = hypotenuse_bin.decode('utf-8')
print('The hypotenuse of a triangle is:', hypotenuse)
conn.close()
