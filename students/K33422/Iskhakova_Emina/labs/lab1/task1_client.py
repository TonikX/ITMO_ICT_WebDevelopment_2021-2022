import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7777))
sock.send('Hello, server! :)'.encode('utf-8'))

d = sock.recv(1024)

print(d.decode('utf-8'))
sock.close()
