import socket

connection = socket.socket()
connection.connect(("127.0.0.1", 14900))

task = "Pifagor: Gipotenuza"
connection.send(task.encode("utf-8"))
data = connection.recv(16384)
print(data.decode())
cathetus = input()
connection.send(cathetus.encode())
data = connection.recv(16384)
connection.close()
print(data.decode())