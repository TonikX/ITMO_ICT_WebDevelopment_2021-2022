import socket


class Client:
    def __init__(self, port):
        self.conn = socket.socket()
        self.conn.connect(('127.0.0.1', port))

    def speak(self):
        while True:
            data = self.conn.recv(1024)
            print(data.decode('utf-8'))
            msg = input()
            self.conn.send(msg.encode('utf-8'))


if __name__ == "__main__":
    client = Client(1433)
    client.speak()
