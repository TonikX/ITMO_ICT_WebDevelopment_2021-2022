import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(16384)
    if not data:
        break
    udata = data.decode("utf-8")
    print(udata)
    conn.send(b'Hello, client \n')