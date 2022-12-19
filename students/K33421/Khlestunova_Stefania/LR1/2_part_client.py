import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 2235))
data = input("Введите длины оснований и высоту через пробел: ")
sock.send(data.encode("utf-8"))
result = sock.recv(1024)
print(result.decode("utf-8"))