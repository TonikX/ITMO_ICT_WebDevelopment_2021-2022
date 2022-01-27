import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(("127.0.0.1", 5667))
client=[]
print("Server started")

while True:
    try:
        data, address = conn.recvfrom(1024)
        if address not in client:
            client.append(address)
        for clients in client:
            if clients == address:
                continue
            conn.sendto(data, clients)
    except KeyboardInterrupt:
        conn.close()
        break