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
    data = client.recv(1024).decode("utf-8").split()
    res = str(int(data[0])*(int(data[1])+int(data[2]))/2)
    res = str.encode(res)
    client.send(res)
    client.close()
