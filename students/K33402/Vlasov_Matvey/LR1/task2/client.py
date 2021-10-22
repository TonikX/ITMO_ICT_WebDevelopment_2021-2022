import socket

conn = socket.socket()
conn.connect(("127.0.0.1", 2334))
input_numbers = input("Enter a, b and c of quadratic equation with space between numbers\n")  # 2 2 -4
conn.send(input_numbers.encode("utf-8"))

data = conn.recv(1024).decode("utf-8")
print(data)
conn.close()
