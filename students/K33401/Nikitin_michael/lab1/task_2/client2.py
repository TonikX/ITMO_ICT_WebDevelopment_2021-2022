import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 14900))


data = sock.recv(16384)
print(data.decode("UTF-8"))
abc = input()
sock.send(abc.encode("UTF-8"))
data = sock.recv(16384)
print(data.decode("UTF-8"))
sock.close()



