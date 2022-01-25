import socket
import sys
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_LINE = 64*1024
MAX_HEADERS = 100

# Класс запрос
class Request:
  def __init__(self, method, target, version, headers, rfile):
    self.method = method
    self.target = target
    self.version = version
    self.headers = headers
    self.rfile = rfile

  @property
  def path(self):
    return self.url.path

  @property
  @lru_cache(maxsize=None)
  def query(self):
    return parse_qs(self.url.query)

  @property
  @lru_cache(maxsize=None)
  def url(self):
    return urlparse(self.target)

# класс Ответ
class Response:
  def __init__(self, status, reason, headers=None, body=None):
    self.status = status
    self.reason = reason
    self.headers = headers
    self.body = body

# класс ошибки
class HTTPError(Exception):
  def __init__(self, status, reason, body=None):
    super()
    self.status = status
    self.reason = reason
    self.body = body


# Класс Сервер
class MyHTTPServer:
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
        except HTTPError as e:
          print('Client serving failed', e)
    finally:
      serv_sock.close()

  def serve_client(self, conn):
    try:
      req = self.parse_request(conn)
      resp = self.handle_request(req)
      self.send_response(conn, resp)
    except ConnectionResetError:
      conn = None
    except HTTPError as e:
      self.send_error(conn, e)

    if conn:
      conn.close()

  def parse_request(self, conn):
    print("parse_request")
    rfile = conn.makefile('rb')
    raw = rfile.readline(MAX_LINE + 1)  # эффективно читаем строку целиком
    if len(raw) > MAX_LINE:
      raise HTTPError(400, 'Bad request')

    req_line = str(raw, 'iso-8859-1')
    req_line = req_line.rstrip('\r\n')
    words = req_line.split()            # разделяем по пробелу
    if len(words) != 3:                 # и ожидаем ровно 3 части
      raise HTTPError(400, 'Bad request')

    method, target, ver = words
    if ver != 'HTTP/1.1':
      raise HTTPError(505, "HTTP Version Not Supported")

    headers = self.parse_headers(rfile)
    host = headers.get('Host')
    if not host:
        raise HTTPError(400, 'Bad request')
    if host not in (self._server_name,
                    f'{self._server_name}:{self._port}'):
      print("Error", host, self._server_name)
      raise HTTPError(404, 'Not found')
    print("parse_headers - OK!!!")
    return Request(method, target, ver, headers, rfile)

  def parse_headers(self, rfile):
    print("parse_headers")
    headers = []
    while True:
      line = rfile.readline(MAX_LINE + 1)
      if len(line) > MAX_LINE:
        raise HTTPError(400, "Bad Request")
      if line in (b'\r\n', b'\n', b''):
        # завершаем чтение заголовков
        break
      headers.append(line)
      if len(headers) > MAX_HEADERS:
        raise HTTPError(400, "Bad Request")
      
    sheaders = b''.join(headers).decode('iso-8859-1')
    return Parser().parsestr(sheaders)
  
  def handle_request(self, req):
    print("handle_request", req.method, req.path)
    if req.method == 'POST':
      return self.handle_post(req)

    if req.method == 'GET':
      return self.handle_get(req)

    raise HTTPError(404, 'Not found')

  def handle_post(self, req): 
    print("POST:", req.query)
    with open("index.html", "rb") as f:
      text = f.read()

      text = text.replace(b"</ul>", b"") 

      name = req.query["name"][0]
      grade = req.query["grade"][0]
      text += b"\t<li>" + name.encode() + b" " + grade.encode() + b"</li>\n</ul>"

      with open("index.html", "wb") as f:
        f.write(text)

    return Response(204, 'Created')

  def handle_get(self, req): 
    print("handle_get", req.headers.get('Accept'))
    accept = req.headers.get('Accept')
    if 'text/html' in accept:
        contentType = 'text/html; charset=utf-8'

        with open("index.html", "rb") as f:
            body = f.read()

    else:
        return Response(406, 'Not Acceptable')

    print("handle_get", body)
    headers = [('Content-Type', contentType),
               ('Content-Length', len(body))]

    
    return Response(200, 'OK', headers, body)

  def send_response(self, conn, resp):
    wfile = conn.makefile('wb')
    status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
    wfile.write(status_line.encode('iso-8859-1'))

    if resp.headers:
      for (key, value) in resp.headers:
        header_line = f'{key}: {value}\r\n'
        wfile.write(header_line.encode('iso-8859-1'))

    wfile.write(b'\r\n')

    if resp.body:
      wfile.write(resp.body)

    wfile.flush()
    wfile.close()

  def send_error(self, conn, err):
    try:
      status = err.status
      reason = err.reason
      body = (err.body or err.reason).encode('utf-8')
    except:
      status = 500
      reason = b'Internal Server Error'
      body = b'Internal Server Error'
    resp = Response(status, reason,
                   [('Content-Length', len(body))],
                   body)
    self.send_response(conn, resp)

if __name__ == '__main__':
  host = "localhost" 
  port = int(input("Введите порт: "))
  name = "localhost"
  serv = MyHTTPServer(host, port, name)

  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    pass