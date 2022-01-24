import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(10)

while True:
    try:
        clientsocket, address = conn.accept()

        data_bin = clientsocket.recv(16384)
        data = data_bin.decode("utf-8")
        data = data.split(" ")

        area = (float(data[0]) + float(data[1])) * float(data[2]) / 2
        clientsocket.send(str(area).encode())

    except ValueError:
        print("Received incorrect data. Waiting for another...")
        clientsocket.close()
    
    except KeyboardInterrupt:
        print("\n")
        conn.close()
        break
