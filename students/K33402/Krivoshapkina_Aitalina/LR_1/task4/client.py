import socket, threading, time

host = socket.gethostbyname(socket.gethostname())
port = 1106

server = (host, port)

s = socket.socket()
s.connect(server)

shutdown = False

username = input("Name: ")

def receving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(data.decode("utf-8"))

                time.sleep(0.2)
        except:
            pass


rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()
s.sendto(("[" + username + "] => join chat ").encode("utf-8"), server)

while not shutdown:
    try:
        message = input()

        if message != "":
            s.sendto(("[" + username + "] :: " + message).encode("utf-8"), server)

        time.sleep(0.2)
    except:
        s.sendto(("[" + username + "] <= left chat ").encode("utf-8"), server)
        shutdown = True


rT.join()
s.close()