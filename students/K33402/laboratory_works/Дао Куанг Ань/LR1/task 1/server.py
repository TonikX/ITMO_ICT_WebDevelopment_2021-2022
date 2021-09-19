import socket


server = socket.socket()
host = '127.0.0.1'
port = 555
server.bind((host,port))

print('Starting server on', host, port)

server.listen(5)

print('Entering infinite loop: hit CTRL-C to exit')
while True:
    client, (client_host, client_port) = server.accept()
    client.send(b'Hello, client \n')
    res = client.recv(1024)
    print(res.decode("utf-8"))

    client.close()
