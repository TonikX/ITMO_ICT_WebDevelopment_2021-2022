import socket
import sys

MAX_LINE = 64*1024

class MyHTTPServer:
  # Параметры сервера
    def __init__(self, host, port, name):
        self.host = host 
        self.port = port 
        self.name = name
  
    def serve_forever(self):
    # 1. Запуск сервера на сокете, 
    # обработка входящих соединений
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            serv_sock.bind((self.host, self.port))
            serv_sock.listen(1)

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            serv_sock.close()

    def serve_client(self, conn):
        # 2. Обработка клиентского подключения
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            self.send_error(conn, e)

        if conn:
            conn.close()

    def parse_request(self, conn):
        # 3. функция для обработки заголовка http+запроса. 
        # Python, сокет предоставляет возможность создать 
        # вокруг него некоторую обертку, которая предоставляет 
        # file object интерфейс. 
        # Это дайте возможность построчно обработать запрос. 
        # Заголовок всегда - первая строка. Первую строку 
        # нужно разбить на 3 элемента 
        # (метод + url + версия протокола). 
        # URL необходимо разбить на адрес и параметры 
        # (isu.ifmo.ru/pls/apex/f?p=2143 , 
        # где isu.ifmo.ru/pls/apex/f, 
        # а p=2143 - параметр p со значением 2143)
        rfile = conn.makefile('rb')
        raw = rfile.readline(MAX_LINE + 1)  
        if len(raw) > MAX_LINE:
            raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()            # разделяем по пробелу
        if len(words) != 3:                 # и ожидаем ровно 3 части
            raise Exception('Malformed request line')

        method, url, ver = words
        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        url, params = url.split("?")
        params = params.split("&")
        params_dct = {}
        for i in range(len(params)):
            # p = {} 
            p_list = params[i].split("=") 
            params_dct[p_list[0]] = p_list[1]
            # params[i] = p 

        dct = {"method": method, "url": url, 
                "params": params_dct, "ver": ver}
        # print(dct)
        return dct


    def handle_request(self, req):
        # 5. Функция для обработки url в соответствии 
        # с нужным методом. В случае данной работы, 
        # нужно будет создать набор условий, 
        # который обрабатывает GET или POST запрос. 
        # GET запрос должен возвращать данные. 
        # POST запрос должен записывать данные на основе 
        # переданных параметров.
        if req["method"] == "GET":
            with open("index.html", "rb") as f:
                data = f.read() 

            # print(data.decode())
            headers = ['Content-Type: text/html\r\n',
                        f'Content-Length: {len(data)}\r\n']

            response = {"code": 200, "reason": "OK", "headers": headers, "body": data}
            return response

        if req["method"] == "POST":
            # print(req["params"]) 
            params = req["params"]
            data = ""
            for param in params:
                st = f'\n\t\t\t<tr>\n\
                \t<td>{param}</td>\n\
                \t<td>{params[param]}</td>\n\
                </tr>'
                data += st

            # читаем текущий index.html            
            with open("index.html", "r") as f:
                text = f.read() 
            
            # находим последнюю запись
            if "</tr>" in text:
                ind = text.rindex("</tr>")+len("</tr>")
                new_text = text[:ind]
                new_text += data  
                new_text += text[ind:]
            
            # записываем новые данные
            with open("index.html", "wb") as f:
                f.write(new_text.encode())

            response = {"code": 204, "reason": "Grade added"}

            return response


    def send_response(self, conn, response_data):
        # 6. Функция для отправки ответа. 
        # Необходимо записать в соединение 
        # status line вида 
        # HTTP/1.1 <status_code> <reason>. 
        # Затем, построчно записать заголовки 
        # и пустую строку, 
        # обозначающую конец секции заголовков.
        # print(response_data)
        wfile = conn.makefile('wb')
        status_line = f"HTTP/1.1 {response_data['code']} {response_data['reason']}\r\n"
        wfile.write(status_line.encode('iso-8859-1'))
        
        if "headers" in response_data:
            for header in response_data["headers"]:
                wfile.write(header.encode('iso-8859-1'))
        
        wfile.write(b'\r\n')

        if "body" in response_data:
            wfile.write(response_data["body"])

        wfile.flush()
        wfile.close()

    def send_error(self, conn, e):
        print("send_error", e)
        try:
            body = e.encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
            
            headers = [f'Content-Length: {len(body)}\r\n']
            resp = {"code": status, "reason": reason, "headers": headers, "body": body}

        self.send_response(conn, resp)


if __name__ == '__main__':
    host = "localhost"
    port = 9090 
    name = "MyServer"

    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
