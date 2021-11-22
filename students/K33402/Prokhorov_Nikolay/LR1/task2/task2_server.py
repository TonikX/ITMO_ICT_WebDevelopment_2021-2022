import argparse
import socket
import traceback

parser = argparse.ArgumentParser(description='Сервер для задачи №2')
parser.add_argument('--host', help='IP хоста', default='localhost')
parser.add_argument('--port', help='Порт хоста', default=8888)

args = parser.parse_args()

print(f'Сервер запущен и принимает запросы по адресу {args.host}:{args.port}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((args.host, args.port))
    sock.listen(1)

    conn, address = sock.accept()

    data = conn.recv(1024).decode()

    try:
        a, b = map(int, data.strip().split())
    except Exception:
        conn.sendall(f'Неверный формат ввода! Ошибка:\n{traceback.format_exc()}!\n'.encode())
    else:
        conn.sendall(f'Теорема Пифагора a**2 + b**2 = c**2: a={a}, b={b}.\nОткуда c**2={a ** 2 + b ** 2}, c={(a ** 2 + b ** 2) ** 0.5}\n'.encode())
