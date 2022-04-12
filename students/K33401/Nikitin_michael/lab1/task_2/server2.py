import socket
import math

def sqr_solution(a ,b ,c ):
    D = b * b - (4 * a * c)
    if D < 0:
        result = f"no roots\n"
    if D == 0:
        x = (-1 * b) / (2 * a)
        result = f"1 root    x={x} \n"
    else:
        D = math.sqrt(D)
        x = (-1 * b - D) / (2 * a)
        x2 = (-1 * b + D) / (2 * a)
        result = f"2 roots   x1={x}, x2={x2} \n"
    return result

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 14900))
sock.listen(1)
cl_sock, addr = sock.accept()
cl_sock.send(bytes(f'enter coefficients "a", "b", "c" of equation "ax^2 + bx + c = y" \n '
                   f'or enter "exit" to finish the program', "utf-8"))
print('connected:', addr)

while True:
    data = cl_sock.recv(16384)
    if not data:
        break
    a, b, c = data.decode("utf-8").split(' ')
    result = sqr_solution(int(a), int(b), int(c))
    cl_sock.send(str(result).encode("UTF-8"))

cl_sock.close()

