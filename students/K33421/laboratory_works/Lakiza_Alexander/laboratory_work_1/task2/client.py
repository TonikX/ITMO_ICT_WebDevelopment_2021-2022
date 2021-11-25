import socket

conn = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM,
                     proto=0)
conn.connect(('127.0.0.1', 53210))

coeffs = input("Enter a, b and c of your quadratic equation separated by space\n")
conn.sendall(bytes(coeffs, "utf-8"))

data = conn.recv(1024)
decoded_data = data.decode("utf-8")

if decoded_data:
    coeffs = coeffs.split()
    print(
        f"Roots of your quadratic equation (({coeffs[0]})*x^2 + ({coeffs[1]})*x + "
        f"({coeffs[2]}) = 0) are:\n{decoded_data}")
conn.close()
