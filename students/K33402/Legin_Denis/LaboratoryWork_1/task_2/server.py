import socket


class Server:
    def __init__(self, port):
        self.sock = socket.socket()
        self.sock.bind(('127.0.0.1', port))  # open socket
        self.sock.listen(10)

    def speak_data(self, msg):
        conn, port = self.sock.accept()
        conn.send(msg.encode('utf-8'))
        data = conn.recv(1026)
        data = data.decode('utf-8')
        try:
            if data == "a":
                answer = self.pifagor_theory(conn)
                msg = 'Гипотенуза = %s' % answer
                conn.send(msg.encode('utf-8'))
            elif data == "b":
                x1, x2 = self.quadratic_equation(conn)
                msg = 'x1 = %s\n' \
                      'x2 = %s' % (x1, x2)
                conn.send(msg.encode('utf-8'))
            elif data == "c":
                area = self.trapezoid_area(conn)
                msg = 'S = %s' % area
                conn.send(msg.encode('utf-8'))
            elif data == "d":
                area = self.parallelogram_area(conn)
                msg = 'S = %s' % area
                conn.send(msg.encode('utf-8'))
            else:
                msg = "Выбран несуществующий функционал"
                conn.send(msg.encode('utf-8'))
        except ValueError:
            msg = "Введено некорректное значение"
            conn.send(msg.encode('utf-8'))
        conn.shutdown(0)
        conn.close()

    def pifagor_theory(self, conn):
        msg = "Введите длину катета a"
        conn.send(msg.encode('utf-8'))
        data_a = conn.recv(1026)
        data_a = data_a.decode('utf-8')
        msg = "Введите длину катета b"
        conn.send(msg.encode('utf-8'))
        data_b = conn.recv(1026)
        data_b = data_b.decode('utf-8')
        return (int(data_a) * int(data_a) + int(data_b) * int(data_b)) ** 0.5

    def quadratic_equation(self, conn):
        msg = "Введите коэффициент a"
        conn.send(msg.encode('utf-8'))
        data_a = conn.recv(1026)
        data_a = data_a.decode('utf-8')
        msg = "Введите коэффициент b"
        conn.send(msg.encode('utf-8'))
        data_b = conn.recv(1026)
        data_b = data_b.decode('utf-8')
        msg = "Введите коэффициент c"
        conn.send(msg.encode('utf-8'))
        data_c = conn.recv(1026)
        data_c = data_c.decode('utf-8')

        discriminant = int(data_b)**2 - (4*int(data_a)*int(data_c))
        x1 = (-int(data_b) + discriminant ** 0.5) / (2*int(data_a))
        x2 = (-int(data_b) - discriminant ** 0.5) / (2 * int(data_a))
        return x1, x2

    def trapezoid_area(self, conn):
        msg = "Введите длину верхнего основания a"
        conn.send(msg.encode('utf-8'))
        data_a = conn.recv(1026)
        data_a = data_a.decode('utf-8')
        msg = "Введите длину нижнего основания b"
        conn.send(msg.encode('utf-8'))
        data_b = conn.recv(1026)
        data_b = data_b.decode('utf-8')
        msg = "Введите высоту h"
        conn.send(msg.encode('utf-8'))
        data_h = conn.recv(1026)
        data_h = data_h.decode('utf-8')

        return ((int(data_a)+int(data_b))/2)*int(data_h)

    def parallelogram_area(self, conn):
        msg = "Введите длину одного из оснований a"
        conn.send(msg.encode('utf-8'))
        data_a = conn.recv(1026)
        data_a = data_a.decode('utf-8')
        msg = "Введите длину высоты к этому основанию h"
        conn.send(msg.encode('utf-8'))
        data_h = conn.recv(1026)
        data_h = data_h.decode('utf-8')

        return int(data_a)*int(data_h)


if __name__ == "__main__":
    server = Server(1433)
    server.speak_data("Я могу выполнить следующие математические операции:\n"
                      "a. Теорема Пифагора\n"
                      "b. Решение квадратного уравнение\n"
                      "c. Поиск площади трапеции\n"
                      "d. Поиск площади параллелограмма")
