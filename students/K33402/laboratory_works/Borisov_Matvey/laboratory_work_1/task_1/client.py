
from socket import *

connection = socket(AF_INET, SOCK_STREAM)
connection.connect(("127.0.0.1", 14900))
connection.send(b"Hello! \n")

data = connection.recv(16384)
decoded_data = data.decode("utf-8")
print("Response: ", decoded_data)
connection.close()
