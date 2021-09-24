import socket
import threading

def read_msg():
    while True:
        data =  conn.recv(1024)
        print(data.decode("utf-8"))
def send_msg():
    conn.sendto(("["+nickname+"]" + msg).encode("utf-8"), server)
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server = "127.0.0.1", 5667
nickname = input("Write your nickname: ")
conn.sendto((nickname+" Connected to server").encode("utf-8"), server)
stream = threading.Thread(target=read_msg)
stream.start()
while True:
    msg = input()
    stream = threading.Thread(target=send_msg)
    stream.start()
