import socket


class Client:
    def __init__(self, port: int):
        self.conn = socket.socket()             # create socket
        self.conn.connect(('127.0.0.1', port))  # connect server

    def speak(self, msg):
        self.conn.send(msg.encode('utf-8'))     # send message
        data = self.conn.recv(1024)             # receive data
        print(data.decode('utf-8'))             # print message
        self.conn.close()                       # close connection


if __name__ == '__main__':
    client = Client(14900)
    client.speak('Hello, server')
