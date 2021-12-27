import socket
import threading


class Client:
    def __init__(self, port: int):
        self.server = '127.0.0.1', port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.conn.bind(('', 0))

    def read(self):
        while True:
            data = self.conn.recv(1024)
            print(data.decode('utf-8'))

    def chat(self):
        print("enter your nickname to start chatting: ")
        nickname = input()
        self.conn.sendto((nickname + ' is online').encode('utf-8'),
                         self.server)
        while True:
            self.conn.sendto((nickname + ': ' + input()).encode('utf-8'),
                             self.server)


if __name__ == '__main__':
    client = Client(14900)
    thread1, thread2 = threading.Thread(target=client.read), threading.Thread(target=client.chat)
    thread1.start(), thread2.start()