import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)
b = ''
while True:
    conn.sendall(bytes(b + f'Введите длинну оснований и высоту: ', "utf-8"))
    data = conn.recv(1024)
    if not data:
        break
    a, b, h = data.decode("utf-8").split(' ')
    s = ((int(a) + int(b)) * int(h)) / 2
    b = f'Площадь трапеции = {s} \n'