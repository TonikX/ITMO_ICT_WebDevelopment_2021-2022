import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 14900))
sock.listen(1)
cl_sock, addr = sock.accept()
print('connected:', addr)

while True:
    data = cl_sock.recv(16384)
    if not data:
        break
    print(data.decode("utf-8"))
    cl_sock.sendall(b'Hello, client!')

cl_sock.close()