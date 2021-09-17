import socket
import threading


class Client:
    def __init__(self, port: int):
        self.server = 'localhost', port                                             # server data
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)                # create socket
        self.conn.connect(('localhost', port))                                      # connect to server

    def read(self):
        while True:
            data = self.conn.recv(1024)
            print(data.decode('utf-8'))                                             #print your friends messages

    def chat(self):
        self.conn.sendto(('client1 is online').encode('utf-8'), self.server)           # notify everyone
        while True:
            self.conn.sendto(('client1 : ' + input()).encode('utf-8'), self.server)    # send message



if __name__ == '__main__':
    client = Client(9090)
    thread1 = threading.Thread(target=client.read)
    thread2 = threading.Thread(target=client.chat)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
