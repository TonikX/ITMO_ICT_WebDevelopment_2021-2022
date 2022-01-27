import socket
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost',14995))
conn.listen()
clientsocket, adress = conn.accept()
data =  clientsocket.recv(16384)
udata = data.decode("utf-8")
if udata == "Hello server! \n":
    print('Hello server!')
    clientsocket.sendall(b'Hello, client')
else:
    print('Expected another message')
conn.close()
