import socket
import math

socket_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_serv.bind(("127.0.0.1", 14900))
socket_serv.listen(1)
connection, address = socket_serv.accept()
print(f"Connected to: {address}")

while True:
    data = connection.recv(16384)
    data = str(data.decode())
    print(data)
    if not data == "Pifagor: Gipotenuza":
        connection.send("Something wrong".encode("utf-8"))
        break
    else:
        connection.send("Input a, b:".encode("utf-8"))
        data = connection.recv(16384)
        data = str(data.decode())

        try:
            a, b = map(int, data.split(' '))
        except:
            connection.send("Input error".encode("utf-8"))

        hypotenuse = math.sqrt(a ** 2 + b ** 2)
        hypotenuse = "Hypotenuse = " + str(hypotenuse)
        connection.send(hypotenuse.encode())
        socket_serv.close()
        break