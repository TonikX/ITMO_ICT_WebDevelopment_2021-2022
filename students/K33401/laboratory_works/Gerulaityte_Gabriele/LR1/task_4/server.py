import socket


class Server:
    def __init__(self, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', port))

    def run(self):
        clients = []                                                 
        while True:
            data, address = self.sock.recvfrom(1024)                  
            print(address[0], address[1])                             
            if address not in clients:
                clients.append(address)                            
            for client in clients:
                if client == address:
                    continue
                self.sock.sendto(data, client) 


if __name__ == '__main__':
    server = Server(14900)
    server.run()