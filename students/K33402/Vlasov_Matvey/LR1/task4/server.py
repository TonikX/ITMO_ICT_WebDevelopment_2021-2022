import socket
import threading

conn = socket.socket()
conn.bind(("127.0.0.1", 2334))
conn.listen(5)


def send_to_everyone(message):
    for client in clients:
        client.send(message)


def listen(client):
    while True:
        try:
            message = client.recv(1024)
            send_to_everyone(message)
        except Exception:
            continue


clients = []
while True:
    try:
        new_client, _ = conn.accept()
        data = new_client.recv(1024)
        if new_client not in clients:
            clients.append(new_client)

        send_to_everyone(data)
        thread = threading.Thread(target=listen, args=[new_client])
        thread.start()
    except KeyboardInterrupt:
        conn.close()

