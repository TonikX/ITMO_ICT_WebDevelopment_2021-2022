import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
conn.connect(('localhost',14995))

n = input("Enter a, b, c coefs\n")
conn.sendall(bytes(n, "utf-8"))

data = conn.recv(16384)
decoded_data = data.decode("utf-8")

if decoded_data:
    n = n.split()
    print(
        f"Roots of your quadratic equation (({n[0]})*x^2 + ({n[1]})*x + "
        f"({n[2]}) = 0) are:\n{decoded_data}")
conn.close()