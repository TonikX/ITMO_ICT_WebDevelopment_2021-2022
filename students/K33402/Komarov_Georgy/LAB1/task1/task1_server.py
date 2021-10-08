import argparse
import socket

parser = argparse.ArgumentParser(description='Task 1 Server')
parser.add_argument('--host', help='Hostname/IP to bind', default='127.0.0.1')
parser.add_argument('--port', help='Port to bind', default=1337)
parser.add_argument('-b', '--buffer', help='Connection buffer size', type=int, default=1024)
args = parser.parse_args()

print(f'Server is listening for TCP connections at {args.host}:{args.port}')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((args.host, args.port))
    sock.listen(1)

    conn, address = sock.accept()

    data = conn.recv(args.buffer).decode()
    print(data, end='')

    if data.strip() == 'Hello, server!':
        conn.sendall('Hello, client!\n'.encode())
    else:
        conn.sendall('Unknown message!\n'.encode())
