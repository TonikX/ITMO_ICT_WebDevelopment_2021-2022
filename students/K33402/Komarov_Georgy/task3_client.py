import argparse
import socket

parser = argparse.ArgumentParser(description='Task 3 Client')
parser.add_argument('--host', help='Hostname/IP to connect', default='127.0.0.1')
parser.add_argument('--port', help='Port to connect', default=1337)
parser.add_argument('-b', '--buffer', help='Connection buffer size', type=int, default=1024)
args = parser.parse_args()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
    data = f'''GET / HTTP/1.1
    Accept: text/html
    Host: {args.host}
    Connection: close''' + '\n\n'

    conn.connect((args.host, args.port))
    conn.sendall(data.encode())

    received = conn.recv(args.buffer).decode()
    print(received, end='')
