import socket

server = socket.socket()
server.bind(('127.0.0.1', 5000))
server.listen(5)

while True:
    client, (client_host, client_port) = server.accept()
    client.recv(4096)
    response_type = 'HTTP/1.1 200 OK\n'
    headers = 'Content-Type: text/html\n\n'

    with open('task_3/index.html', 'r') as f:
        body = f.read()
    response = response_type + headers + body
    client.send(response.encode('utf-8'))
    client.close()
