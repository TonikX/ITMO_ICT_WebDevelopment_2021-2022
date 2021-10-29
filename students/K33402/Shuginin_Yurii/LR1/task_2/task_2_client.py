import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))

data = input("Enter first trapezoid base: ").replace(" ", "")
data += " " + input("Enter second trapezoid base: ").replace(" ", "")
data += " " + input("Enter trapezoid height: ").replace(" ", "")
conn.send(data.encode())

area_bin = conn.recv(16384)
area = area_bin.decode("utf-8")

if area:
    print("The trapezoid area is: " + area + "\n")
else:
    print("Server couldn't calculate the area. \n")

conn.close()
