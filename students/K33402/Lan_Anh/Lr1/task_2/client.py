import socket

task = "Square Equations"
encoding = "UTF-8"
sock = socket.socket()
sock.connect(('localhost', 9090))

sock.send(task.encode(encoding))
data = sock.recv(1024)
print(data.decode("UTF-8"))

numbers = input()

sock.send(numbers.encode(encoding))
data = sock.recv(1024)
print(data.decode("UTF-8"))
sock.close()
