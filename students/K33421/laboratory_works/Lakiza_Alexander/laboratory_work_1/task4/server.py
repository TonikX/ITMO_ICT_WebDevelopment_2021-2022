import socket

conn = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
conn.bind(("127.0.0.1", 53210))


def run():
    clients = []
    while True:
        try:
            data, client_address = conn.recvfrom(2048)
            if client_address not in clients:
                clients.append(client_address)
            for client in clients:
                if client != client_address:
                    conn.sendto(data, client)
        except KeyboardInterrupt:
            conn.close()
            break


if __name__ == "__main__":
    run()
