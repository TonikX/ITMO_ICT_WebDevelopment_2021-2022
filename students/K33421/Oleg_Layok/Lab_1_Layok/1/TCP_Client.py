import socket

conn = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)
conn.connect(('localhost',14995))

conn.sendall(b"Hello server! \n")

data = conn.recv(16384)
decoded_data = data.decode("utf-8")

if decoded_data:
    print(f"Received from server:\n{decoded_data}")
conn.close()