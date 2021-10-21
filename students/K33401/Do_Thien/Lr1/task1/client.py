import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((socket.gethostname(), 16900))

serversocket.send(b"Hello server! \n")
data = serversocket.recv(1024)
print("Server: " + data.decode("utf-8"))
serversocket.close()
