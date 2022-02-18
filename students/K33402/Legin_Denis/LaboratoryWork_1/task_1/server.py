import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket()           # create socket
        self.sock.bind(('127.0.0.1', port))   # open socket
        self.sock.listen(10)                  # open connection queue

    def speak(self, msg):
        conn, port = self.sock.accept()       # accept connection
        data = conn.recv(1024)                # receive data
        print(data.decode('utf-8'))           # print message
        conn.send(msg.encode('utf-8'))        # send message
        conn.close()                          # close socket


if __name__ == '__main__':
    server = Server(14890)
    server.speak('Hello, Client')
