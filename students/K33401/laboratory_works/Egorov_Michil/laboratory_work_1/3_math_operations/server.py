from typing import Tuple
import socket

from base import BaseServer


class MathServer(BaseServer):
    def solve_pythagorean(self, first_cathetus: float, second_cathetus: float) -> str:
        hypotenuse = (first_cathetus ** 2 + second_cathetus ** 2) ** 0.5
        return "Гипотенуза прямоугольного треугольника с катетами a={} и b={}: {}".format(
            first_cathetus,
            second_cathetus,
            hypotenuse
        )

    def solve_quadratic_equation(self, a: float, b: float, c: float) -> str:
        discriminant = b ** 2 - 4 * a * c

        if a == 0:
            raise ValueError("Уравнение не является квадратичным. ")

        x1 = (b - discriminant ** 0.5) / (2 * a)
        x2 = (b + discriminant ** 0.5) / (2 * a)

        return "Решения квадратного уравнения {}*x^2+({})*x+({}): {} и {}".format(a, b, c, x1, x2)

    def solve_trapezoid_area(self, a: float, b: float, h: float) -> str:
        if a <= 0 or b <= 0 or h <= 0:
            raise ValueError("Стороны трапеции могут быть только положительными")

        area = (a + b) / 2 * h

        return "Площаль трапеции со сторонами a={} и b={} и высотой h={}: {}".format(a, b, h, area)

    def solve_parallelogram_area(self, a: float, h: float) -> str:
        if a <= 0 or h <= 0:
            raise ValueError("Стороны трапеции могут быть только положительными")

        return "Площадь параллелограмма со стороной a={} и высотой h={}: {}".format(a, h, a * h)

    def _handle(self, client_socket: socket.socket, address: Tuple[str, int], data: str) -> None:
        """
        Данные будут вида "op_name op_arguments"
        Сначала идет название операции, а затем, через пробел, нужные аргументы

        a) Теорема Пифагора
        :param op_name: pythagorean
        :param op_arguments: два числа записанные через пробел - катеты прямоугольного треугольника
        :return: вещественное число: сторона гипотенузы

        б) Решение квадратного уравнения.
        :param op_name: quadratic_equation
        :param op_arguments: три числа записанные через пробел - коэффиценты a, b, c уравнения a*x^2 + b*x + c = 0
        :return: два вещественных числа: решения уравнения

        в) Поиск площади трапеции
        :param op_name: trapezoid_area
        :param op_arguments: три числа записанные через пробел - длины параллельных сторон и высота трапеции
        :return: вещественное число: площадь трапеции

        г) Поиск площади параллелограмма
        :param op_name: parallelogram_area
        :param op_arguments: два числа - длины стороны и падающей на нее высоты параллелограмма
        :return: вещественное число: площадь параллеллограмма
        """

        op_name, *args = data.split()
        method = 'solve_' + op_name

        if not hasattr(self, method):
            raise ValueError(f'Метода {method} не существует')

        handler = getattr(self, method)

        try:
            args = list(map(float, args))
            answer = handler(*args)
        except (TypeError, ValueError):
            answer = 'Неверный формат входных данных'
        except Exception as e:
            answer = repr(e)

        self._send_message(client_socket, answer)


if __name__ == "__main__":
    server = MathServer("127.0.0.1", 8000)
    server.loop()
