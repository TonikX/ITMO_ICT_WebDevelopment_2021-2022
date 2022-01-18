import socket

PORT = 16900
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
    except:
        serversocket.close()
        break
