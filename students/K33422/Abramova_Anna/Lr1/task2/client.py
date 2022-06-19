import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14000))

a = input("Катет а: ")
b = input("Катет b: ")

conn.send(' '.join([a, b]).encode())
data = conn.recv(1024)
print(data.decode('utf-8'))

conn.close()
