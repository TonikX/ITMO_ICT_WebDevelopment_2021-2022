import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create socket
        self.sock.bind(('127.0.0.1', port))                           # open socket

    def run(self):
        clients = []                                                  # create users array
        while True:
            data, address = self.sock.recvfrom(1024)                  # receive data
            print(address[0], address[1])                             # users' addresses
            if address not in clients:
                clients.append(address)                               # add new user
            for client in clients:
                if client == address:
                    continue
                self.sock.sendto(data, client)                        # send data


if __name__ == '__main__':
    server = Server(14900)
    server.run()
