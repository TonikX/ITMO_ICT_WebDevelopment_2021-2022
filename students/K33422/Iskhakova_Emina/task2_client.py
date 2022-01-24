import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))

while True:
    try:
        data = sock.recv(1024)
        if not data:
            sock.close()
            break
        print(data.decode("utf-8"))
        sock.sendall(bytes(input(), "utf-8"))
    except KeyboardInterrupt:
        sock.close()
        break

