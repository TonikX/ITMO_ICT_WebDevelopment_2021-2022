import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket()                    # create socket
        self.sock.bind(('127.0.0.1', port))            # open socket
        self.sock.listen(1)                            # open connection queue

    def load(self):
        conn, port = self.sock.accept()                # accept connection
        with open('index.html', 'r') as file:          # open file
            response_type = 'HTTP/1.0 200 OK\n'        # response type
            headers = 'Content-Type: text/html\n\n'    # headers
            body = file.read()                         # read data
            response = response_type + headers + body  # form response
            conn.send(response.encode('utf-8'))        # send data
        conn.close()                                   # close connection


if __name__ == '__main__':
    server = Server(14900)
    server.load()
