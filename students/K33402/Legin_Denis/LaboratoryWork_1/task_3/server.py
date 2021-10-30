import socket


class Server:
    def __init__(self, port):
        self.sock = socket.socket()
        self.sock.bind(('127.0.0.1', port))  # open socket
        self.sock.listen(10)

    def html_load(self):
        while True:
            client, (client_host, client_port) = self.sock.accept()
            print('Got connection from', client_host, client_port)
            client.recv(1026)
            response_type = 'HTTP/1.0 200 OK\n'
            headers = 'Content-Type: text/html\n\n'
            with open('index.html', 'r') as r:
                body = r.read()
            response = response_type + headers + body
            client.send(response.encode('utf-8'))
            client.close()



if __name__ == "__main__":
    server = Server(1434)
    server.html_load()
