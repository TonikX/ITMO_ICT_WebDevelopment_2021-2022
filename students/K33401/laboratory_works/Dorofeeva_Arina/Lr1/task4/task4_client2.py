import socket
import threading


class Client:
    def __init__(self, port: int):
        self.server = '127.0.0.1', port                                    # server data
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)       # create socket
        self.conn.bind(('', 0))                                            # open socket

    def read(self):
        while True:
            data = self.conn.recv(1024)
            print(data.decode('utf-8'))

    def chat(self):
        print("enter your nickname to start chatting: ")
        nickname = input()                                                 # get nickname
        self.conn.sendto((nickname + ' is online').encode('utf-8'),        # notify everyone
                         self.server)
        while True:
            self.conn.sendto((nickname + ': ' + input()).encode('utf-8'),  # send message
                             self.server)


if __name__ == '__main__':
    client = Client(14900)
    thread1, thread2 = threading.Thread(target=client.read), threading.Thread(target=client.chat)
    thread1.start(), thread2.start()
