import argparse
import socket

parser = argparse.ArgumentParser(description='Task 2 Client')
parser.add_argument('--host', help='Hostname/IP to connect', default='127.0.0.1')
parser.add_argument('--port', help='Port to connect', default=1337)
parser.add_argument('-b', '--buffer', help='Connection buffer size', type=int, default=1024)
args = parser.parse_args()

inp = input('Enter quadratic equation coefficients (a, b, c) divided by space. Such as:\n1 2 1\n>> ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    conn.connect((args.host, args.port))
    conn.sendall(inp.encode())

    received = conn.recv(args.buffer).decode()
    print(received, end='')
