import socket

host = "127.0.0.1"
port = 9091

s = socket.socket()
s.connect((host, port))

data = input("Enter a, b, h (meters) separated by a space: ")
s.send(data.encode("utf-8"))

response = s.recv(16384)
print("Result: " + response.decode("utf-8"))

s.close()