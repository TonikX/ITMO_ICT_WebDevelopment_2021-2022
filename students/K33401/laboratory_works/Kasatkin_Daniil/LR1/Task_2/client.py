import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 8000))
message = input("Введите катеты через пробел : ")
conn.send(bytes(message, "utf-8"))
data = conn.recv(1024).decode('utf-8')
print(data)
conn.close()
