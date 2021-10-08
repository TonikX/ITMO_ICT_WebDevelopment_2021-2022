from socket import *


def run():
    clients = []
    while True:
        try:
            data, client_address = connection.recvfrom(16384)
            if client_address not in clients:
                clients.append(client_address)
            for client in clients:
                if client == client_address:
                    continue
                connection.sendto(data, client)
        except KeyboardInterrupt:
            connection.close()
            break
        except:
            continue


connection = socket(AF_INET, SOCK_DGRAM)
connection.bind(("127.0.0.1", 14900))
run()
