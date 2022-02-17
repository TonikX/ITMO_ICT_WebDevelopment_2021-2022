import socket

HOST, PORT = "127.0.0.1", 14900

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect((HOST, PORT))
a_b_h = input("Write three numbers(A B H ) with space : ")
conn.send(a_b_h.encode("utf-8"))

data = conn.recv(16384)

print("The area of a trapezoidresult: " + data.decode("utf-8"))

conn.close()

