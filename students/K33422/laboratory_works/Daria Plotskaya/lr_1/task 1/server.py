import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 14900))
s.listen(5)


while True:
	clientsocket, address = s.accept()
	clientsocket.send(bytes('Hello, client', 'utf-8'))
	data = clientsocket.recv(1024)
	print(data.decode("utf-8"))

s.close()
