import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080

server.bind((host, port))
server.listen()

while True:
    conn, addr = server.accept()

    page = open('index.html')
    content = page.read()
    page.close()

    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(content),
    }

    response_headers_raw = ''.join(f'{key}: {value}\n' for key, value in response_headers.items())

    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'

    conn.sendall(f'{response_proto} {response_status} {response_status_text}{response_headers_raw}\n{content}'.encode())

    conn.close()
