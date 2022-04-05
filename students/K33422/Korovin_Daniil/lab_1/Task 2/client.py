import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))

while True:
    data = sock.recv(1024)
    if not data:
        sock.close()
        break
    print(data.decode("utf-8"))
    sock.sendall(bytes(input(), "utf-8"))


