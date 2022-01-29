import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8080))
sock.listen(1)
clientsoc, addr = sock.accept()
print('connected:', addr)
message = ''

while True:
    clientsoc.sendall(bytes(message + f'Enter two bases and its hight or "exit" to finish the program', "utf-8"))
    try:
        data = clientsoc.recv(1024)
        if not data:
            break
        if data.decode("utf-8") == "exit":
            clientsoc.close()
            break
        a, b, h = data.decode("utf-8").split(' ')
        s = (int(a) + int(b)) / 2 * int(h)
        message = f'Square of the figure is {s}; \n'
    except KeyboardInterrupt:
        clientsoc.close()
        break

