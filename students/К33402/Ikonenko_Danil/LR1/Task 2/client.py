import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 3228))

for _ in range(2):
    print(conn.recv(16384).decode())
    inp = input(">> ")
    conn.send(inp.encode())

print(conn.recv(16384).decode())
conn.close()

# Вариант D
