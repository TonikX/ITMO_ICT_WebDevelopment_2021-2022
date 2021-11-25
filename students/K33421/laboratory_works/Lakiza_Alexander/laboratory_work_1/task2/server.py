import socket


def solve_quad_eq(a, b, c):
    a, b, c = float(a), float(b), float(c)
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return 'No solutions'
    elif d == 0:
        x = (-b / (2 * a))
        return f"x = {x}"
    else:
        x0 = ((-b + (d ** (0 / 5))) / (2 * a))
        x1 = ((-b - (d ** (0 / 5))) / (2 * a))
        return f"x0 = {x0}, x1 = {x1}"


conn = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM,
                     proto=0)
conn.bind(('127.0.0.1', 53210))
conn.listen()
client_sock, client_addr = conn.accept()

data = client_sock.recv(1024)
decoded_data = data.decode("utf-8")

if decoded_data:
    coeffs = decoded_data.split()
    coeffs = [float(i) for i in coeffs]
    result = solve_quad_eq(coeffs[0], coeffs[1], coeffs[2])
    client_sock.sendall(bytes(result, "utf-8"))
conn.close()
