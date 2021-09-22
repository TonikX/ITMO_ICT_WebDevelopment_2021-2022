import argparse
import socket
from email.utils import formatdate

parser = argparse.ArgumentParser(description='Task 3 Server')
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

    with open('index.html') as f:
        content = f.read()

        response = f'''HTTP/1.1 200 OK
Server: myserver/0.0.1
Date: {formatdate(timeval=None, localtime=False, usegmt=True)}
Content-Type: text/html
Content-Length: {len(content)}''' + '\n\n' + content

        conn.sendall(response.encode())
