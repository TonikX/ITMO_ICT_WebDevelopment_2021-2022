import socket
import time
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 1234))
a = str.encode(input('введите название желаемой функции \n'
      'Треугольник Пифагора - 1\n'
      'Квадратное уравнение - 2\n'
      'Площадь трапеции - 3\n'
      'Площадь параллелограмма - 4\n'))
conn.send(a)
while True:
      data = conn.recv(22222)
      udata = data.decode("utf-8")
      print(udata)
      answer = str.encode(input())
      conn.send(answer)
conn.close