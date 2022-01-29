import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 7777))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
    conn.send('Hello, client! :)'.encode('utf-8'))

conn.close()
