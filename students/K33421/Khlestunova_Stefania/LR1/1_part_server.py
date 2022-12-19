import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 2234))
s.listen(5)

while True:
    try:
        client_socket, addr = s.accept()
        print(f"Connection to {addr} done!")
        data = client_socket.recv(1024)
        updata = data.decode('utf-8')
        print(updata)
        client_socket.send(bytes("Hello, client!", "utf-8"))
    except KeyboardInterrupt:
        s.close()
        break
    
    