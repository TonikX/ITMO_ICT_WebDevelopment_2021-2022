
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind(("127.0.0.1", 14900))
connection.listen()

client_socket, address = connection.accept()
data = client_socket.recv(16384)
decoded_data = data.decode("utf-8")
print("Data: " + decoded_data)

send_data = b"Hello client"
client_socket.sendto(send_data, address)
