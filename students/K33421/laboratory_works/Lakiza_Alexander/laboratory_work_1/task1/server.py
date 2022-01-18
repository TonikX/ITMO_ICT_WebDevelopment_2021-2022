import socket

conn = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM,
                     proto=0)
conn.bind(('127.0.0.1', 53210))
conn.listen()
client_sock, client_addr = conn.accept()

data = client_sock.recv(1024)
decoded_data = data.decode("utf-8")

if decoded_data:
    print(f"Recieved from client:\n{decoded_data}")
    client_sock.sendall(b'Hello, client')
conn.close()
