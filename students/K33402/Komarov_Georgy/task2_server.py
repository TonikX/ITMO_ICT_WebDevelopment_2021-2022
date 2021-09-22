import argparse
import socket
from math import sqrt

parser = argparse.ArgumentParser(description='Task 2 Server')
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

    try:
        a, b, c = map(int, data.strip().split())
    except:
        conn.sendall('Wrong input format!\n'.encode())
    else:
        D = b**2 - 4 * a * c
        if D > 0:
            x1, x2 = (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
            conn.sendall(f'Roots are: {x1}, {x2}\n'.encode())
        elif D == 0:
            x = (-b) / (2 * a)
            conn.sendall(f'Root is: {x}\n'.encode())
        else:
            conn.sendall(f'No real roots found.'.encode())
