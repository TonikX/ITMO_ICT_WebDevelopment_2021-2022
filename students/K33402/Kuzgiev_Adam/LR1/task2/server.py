import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

while True:
    try:
        clientsocket, adress = conn.accept()
        data = clientsocket.recv(16384)
        udata = data.decode("utf-8")
        print("Calculating the area of a trapezoid for data: " + udata)
        a, b, h = [float(num) for num in udata.split(" ")]
        result = ((a+b)/2)*h
        massage = str(result)
        clientsocket.send(massage.encode("utf-8"))
    except KeyboardInterrupt:
        conn.close()