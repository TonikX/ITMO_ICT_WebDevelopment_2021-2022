import socket

HOST, PORT = "127.0.0.1", 14900

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(10)

sock, address = conn.accept()
client_data = sock.recv(16384)
client_data = client_data.decode("utf-8")
print(client_data)
msg_for_client = "Hello, Client!"
sock.send(msg_for_client.encode("utf-8"))
conn.close()