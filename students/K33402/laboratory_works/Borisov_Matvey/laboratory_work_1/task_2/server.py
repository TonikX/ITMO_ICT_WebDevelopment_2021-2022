
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 14900))
server.listen(10)

while True:
    try:
        client, address = server.accept()
        data = client.recv(16384)
        data = data.decode("utf-8").split(" ")
        side = int(data[0])
        height = int(data[1])

        send_data = bytes("Area is " + str(side * height), "utf-8")
        client.sendto(send_data, address)
    except KeyboardInterrupt:
        server.close()
        break
    except:
        client.send(b"Error: not correct data")



