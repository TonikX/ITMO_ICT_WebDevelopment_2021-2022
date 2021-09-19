import socket
import sys


conn = socket.socket()
host = '127.0.0.1'
port = 555

conn.connect((host,port))


data = input('Enter 3 values of h, a, b in the corresponding order:')
if not data:
    conn.close()
    sys.exit(1)

data = str.encode(data)
conn.send(data)
data2 = conn.recv(1024)
print("Result:",data2.decode("utf-8"))


conn.close()