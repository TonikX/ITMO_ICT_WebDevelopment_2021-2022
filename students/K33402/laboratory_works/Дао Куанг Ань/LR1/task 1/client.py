import socket

conn = socket.socket()
host = '127.0.0.1'
port = 555

conn.connect((host,port))
conn.send(b"Hello, server \n")

result = conn.recv(1024)
print(result.decode("utf-8") )

conn.close()