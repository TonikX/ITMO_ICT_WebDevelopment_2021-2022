import socket

conn = socket.socket()
conn.bind(("127.0.0.1", 2334))
conn.listen(1)

client, (client_host, client_port) = conn.accept()
with open('index.html', 'r') as f:
    response_type = 'HTTP/1.0 200 OK\n'
    headers = 'Content-Type: text/html\n\n'
    body = f.read()
    response = response_type + headers + body
    client.send(response.encode('utf-8'))

conn.close()
