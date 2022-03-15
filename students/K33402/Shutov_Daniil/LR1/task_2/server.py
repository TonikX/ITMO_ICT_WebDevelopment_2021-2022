# Option "a". Pythagorean theorem
import socket
import math

server = socket.socket()
host = '127.0.0.1'
port = 5000
server.bind((host, port))
server.listen(3)


conn, address = server.accept()
first_side_bin = conn.recv(200)
second_side_bin = conn.recv(200)
first_side = first_side_bin.decode('utf-8')
second_side = second_side_bin.decode('utf-8')
hypotenuse = math.sqrt(int(first_side)**2 + int(second_side)**2)
conn.send(str(hypotenuse).encode())
conn.close()
