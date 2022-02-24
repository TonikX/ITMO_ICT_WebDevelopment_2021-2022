import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket()               # create socket
        self.sock.bind(('127.0.0.1', port))       # open socket
        self.sock.listen(1)                       # open connection queue

    def calculate(self):
        conn, port = self.sock.accept()           # accept connection
        params = conn.recv(1024)                  # receive data
        a, h = params.decode('utf-8').split(',')  # get parameters
        ans = str(int(a) * int(h))                # calculate square
        conn.send(ans.encode('utf-8'))            # send data
        conn.close()                              # close socket


if __name__ == '__main__':
    server = Server(14900)
    server.calculate()
