from socket import *

while True:
    try:
        side = int(input("Enter parallelogram side: "))
        height = int(input("Enter parallelogram height: "))
        break
    except:
        print("Enter correct data\n")

connection = socket(AF_INET, SOCK_STREAM)
connection.connect(("127.0.0.1", 14900))
data = str(side) + " " + str(height)
connection.send(bytes(data, "utf-8"))

data = connection.recv(16384)
decoded_data = data.decode("utf-8")
print("Response: ", decoded_data)
connection.close()
