import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 14900))

while True:
    data = sock.recv(16384)
    if not data:
        break
    print(data.decode("utf-8"))

sock.close()
