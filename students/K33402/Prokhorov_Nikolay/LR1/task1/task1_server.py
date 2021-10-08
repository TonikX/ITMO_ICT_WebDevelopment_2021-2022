import argparse
import socket

parser = argparse.ArgumentParser(description='Сервер для задачи №1')
parser.add_argument('--host', help='IP хоста', default='localhost')
parser.add_argument('--port', help='Порт хоста', default=8888)

args = parser.parse_args()

print(f'Сервер запущен и принимает запросы по адресу {args.host}:{args.port}')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((args.host, args.port))
    sock.listen(1)

    conn, address = sock.accept()

    data = conn.recv(1024).decode()
    print(data, end='')

    if data.strip() == 'Hello, server!':
        conn.sendall('Hello, client!\n'.encode())
