import socket


class Client:
    def __init__(self, port: int):
        self.conn = socket.socket()                    # create socket
        self.conn.connect(('127.0.0.1', port))         # connect server

    def calculate(self, a: int, h: int):
        self.conn.sendall(bytes(f'{a},{h}', 'utf-8'))  # send data
        data = self.conn.recv(1024)                    # receive data
        print('the square is:', data.decode('utf-8'))  # print answer
        self.conn.close()                              # close connection


if __name__ == '__main__':
    client = Client(14900)
    client.calculate(int(input('input a: ')), int(input('input h: ')))
