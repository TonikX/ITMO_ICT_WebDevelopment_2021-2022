import socket
from time import sleep

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9000))
response = conn.recv(1024)
print(response.decode())
# sleep(10)

conn.close()
