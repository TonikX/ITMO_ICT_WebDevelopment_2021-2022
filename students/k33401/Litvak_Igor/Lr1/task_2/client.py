# Variant d. - area of parallelogram

import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 14900))

# Loop over twice because there are two inputs
for _ in range(2):
    print(conn.recv(16384).decode())  # Message from server
    inp = input(">> ")  # Get base length from user
    conn.send(inp.encode())  # Send it back

print(conn.recv(16384).decode())
conn.close()
