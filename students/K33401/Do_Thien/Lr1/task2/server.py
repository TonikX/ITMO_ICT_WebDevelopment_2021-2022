import socket
import pickle

PORT = 14900
HOST = socket.gethostname()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(5)

while True:
    try:
        conn, addr = serversocket.accept()
        print(f"Connected {addr}!")
        msg = ""
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode("utf-8")
        print("Client: " + msg)
        conn.send(b"Hello client!")

        data_trapezoid = conn.recv(1024)
        trapezoid = pickle.loads(data_trapezoid)
        area = 1/2*trapezoid[2]*(trapezoid[0] + trapezoid[1])
        conn.send(pickle.dumps(area))

    except:
        serversocket.close()
        break
