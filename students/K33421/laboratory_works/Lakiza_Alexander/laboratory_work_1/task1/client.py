import socket

conn = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM,
                     proto=0)
conn.connect(('127.0.0.1', 53210))

conn.sendall(b'Hello, server')

data = conn.recv(1024)
decoded_data = data.decode("utf-8")

if decoded_data:
    print(f"Received from server:\n{decoded_data}")
conn.close()
