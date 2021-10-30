import socket
import sys


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            proto=0)
        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            serv_sock.close()

    # 1. Запуск сервера на сокете, обработка входящих соединений

    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None

        if conn:
            conn.close()

    # 2. Обработка клиентского подключения

    def parse_request(self, conn):
        pass

    # 3. функция для обработки заголовка http+запроса. Python, сокет предоставляет возможность создать вокруг него
    # некоторую обертку, которая предоставляет file object интерфейс. Это дайте возможность построчно обработать
    # запрос. Заголовок всегда - первая строка. Первую строку нужно разбить на 3 элемента  (метод + url + версия
    # протокола). URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143 ,
    # где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)

    def parse_headers(self):
        pass

    # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления пустой
    # строки и сохранить их в массив.

    def handle_request(self, req):
        pass

    # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор
    # условий, который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен
    # записывать данные на основе переданных параметров.

    def send_response(self, conn, resp):
        pass


# 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
# Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.

if __name__ == '__main__':
    hostS = "127.0.0.1"
    portS = 1028
    name = 'index.html'
    serv = MyHTTPServer(hostS, portS, name)
