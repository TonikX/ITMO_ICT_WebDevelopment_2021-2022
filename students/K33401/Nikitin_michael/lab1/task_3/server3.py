import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 14900))
sock.listen(1)
cl_sock, addr = sock.accept()
print('connected:', addr)
with open('index.html', 'r') as file:
   html = file.read()
   cl_sock.sendall(bytes(f'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{html}', 'utf-8'))

cl_sock.close()