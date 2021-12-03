import socket
import sys

MAX_LINE = 64*1024

class MyHTTPServer:
  # Параметры сервера
  def __init__(self, _host, _port, _name):
        self.host = host
        self.port = port
        self.server_name = _name
  
  def serve_forever(self):
    # 1. Запуск сервера на сокете, обработка входящих соединений
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
    
    try:
        serv_sock.bind((self.host, self.port))
        serv_sock.listen(1)

        while True:
            conn, _ = serv_sock.accept() # ожидаем подключение клиента
            try:
                self.serve_client(conn) 
            except Exception as e:
                print('Client serving failed', e)
    finally:
        serv_sock.close()

  def serve_client(self, conn):
    # 2. Обработка клиентского подключения
    try:
      req = self.parse_request(conn) # разбор запроса
      resp = self.handle_request(req) # формирование ответа
      self.send_response(conn, resp) # отправляет ответ
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
    # file object интерфейс. Это дайте возможность 
    # построчно обработать запрос. 
    # Заголовок всегда - первая строка. 
    # Первую строку нужно разбить на 3 элемента  
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
    
    words = req_line.split()

    method, url, ver = words
    print(url)
    dct = {} 
    if method == "GET":
      dct["method"] = "GET"
    elif method == "POST":
      dct["method"] = "POST"
      params = {} 
      a = url.split("?")[1]
      a = a.split("&")
      name = a[0].split("=")[1]
      grade = a[1].split("=")[1]
      params["name"] = name 
      params["grade"] = grade
      dct["params"] = params
     
    print("parse_request... OK!")
    return dct

  def parse_headers(self, req):
    # 4. Функция для обработки headers. 
    # Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
    pass

  def handle_request(self, req):
    # 5. Функция для обработки url в соответствии с нужным 
    # методом. В случае данной работы, нужно будет создать 
    # набор условий, который обрабатывает GET или POST запрос.
    # GET запрос должен возвращать данные. 
    # POST запрос должен записывать данные на основе 
    # переданных параметров.
    if req["method"] == 'GET':
      with open("index.html", "rb") as f:
        text = f.read()

      headers = [
                  f'Content-Length {len(text)}\r\n',
                ]
      
      response = {
        "status": 200,
        "reason": "OK",
        "headers": headers,
        "text": text
      }
    if req["method"] == 'POST': 
      with open("index.html", "rb") as f:
        text = f.read()

      text = text.replace(b"</ul>", b"") 

      text += b"\t<li>" + req["params"]["name"].encode() + b" " + req["params"]["grade"].encode() + b"</li>\n</ul>"

      with open("index.html", "wb") as f:
        f.write(text)

      headers = [
                  f'Content-Length {len(text)}\r\n',
                ]
      
      response = {
        "status": 200,
        "reason": "OK",
        "headers": headers,
        "text": text
      }

    print("handle_request... OK!")
    return response

  def send_response(self, conn, resp):
    # 6. Функция для отправки ответа. 
    # Необходимо записать в соединение 
    # status line вида HTTP/1.1 <status_code> <reason>. 
    # Затем, построчно записать заголовки 
    # и пустую строку, обозначающую конец секции 
    # заголовков. 
    wfile = conn.makefile('wb')
    status_line = f'HTTP/1.1 {resp["status"]} {resp["reason"]}\r\n'
    wfile.write(status_line.encode('iso-8859-1'))

    if "headers" in resp:
      for header in resp["headers"]:
        wfile.write(header.encode('iso-8859-1'))
    
    # wfile.write(b'\r\n')

    if "text" in resp:
      wfile.write(resp["text"])

    wfile.flush()
    wfile.close()
    print("send_response... OK!")


  def send_error(self, conn, err):
    # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>. Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    try:
      status = err.status
      reason = err.reason
      body = (err.body or err.reason).encode('utf-8')
    except:
      status = 500
      reason = b'Internal Server Error'
      body = b'Internal Server Error'
    print(err)
    # resp = Response(status, reason,
    #                [('Content-Length', len(body))],
    #                body)
    # self.send_response(conn, resp)


if __name__ == '__main__':
  host = "localhost" 
  port = int(input("Введите порт: "))
  name = "MyServer"
  serv = MyHTTPServer(host, port, name)

  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    pass

