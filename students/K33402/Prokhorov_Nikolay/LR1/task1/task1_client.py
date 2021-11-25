import argparse
import socket

parser = argparse.ArgumentParser(description='Клиент для задачи №1')
parser.add_argument('--host', help='IP хоста', default='localhost')
parser.add_argument('--port', help='Порт хоста', default=8888)

args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((args.host, args.port))
    conn.sendall('Hello, server!\n'.encode())

    received = conn.recv(1024).decode()
    print(received, end='')
