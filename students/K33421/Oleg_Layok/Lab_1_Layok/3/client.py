import socket

conn = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM,
                     proto=0)
conn.connect(('127.0.0.1',5000))
data = conn.recv(16384)
decoded_data = data.decode("utf-8")

if decoded_data:
    print(f"Received from server:\n{decoded_data}")
conn.close()