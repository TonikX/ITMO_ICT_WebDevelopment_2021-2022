import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 14900))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	data = clientsocket.recv(1024)
	numbers = data.decode("utf-8")
	a = int(numbers[0])
	b = int(numbers[1])
	h = int(numbers[2])
	sq = (a+b)/2*h
	clientsocket.send(bytes(str(sq), "utf-8"))
s.close()
