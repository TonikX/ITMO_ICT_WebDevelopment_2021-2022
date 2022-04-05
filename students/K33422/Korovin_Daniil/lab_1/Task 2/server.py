import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)
b = ''
while True:
    conn.sendall(bytes(b + f'Введите сторону и опущенную диагональ: ', "utf-8"))
    data = conn.recv(1024)
    if not data:
        break
    a, h = data.decode("utf-8").split(' ')
    s = int(a) * int(h)
    b = f'Площадь параллелограма = {s} \n'

