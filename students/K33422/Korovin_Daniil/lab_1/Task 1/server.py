import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    conn.sendall(b'Hello, client!')

conn.close()