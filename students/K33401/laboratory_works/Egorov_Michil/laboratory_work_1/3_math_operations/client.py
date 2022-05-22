import socket

TASKS = [
    'pythagorean 3 4',
    'quadratic_equation 1 2 1',
    'trapezoid_area 4 5 3',
    'parallelogram_area 4 2',
    '-1 2 4 asdasd',
    'pythagorean ',
    'quadratic_equation 0 2 1',
    'trapezoid_area -4 5 0',
    'trapezoid_area 4 asdg',
    'trapezoid_area 4',
    'parallelogram_area 4 0',
]

if __name__ == "__main__":
    for task in TASKS:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(("127.0.0.1", 8000))
        conn.send(task.encode('utf-8'))
        server_answer = conn.recv(16348).decode('utf-8')
        print(task, ':', server_answer)
        conn.close()
