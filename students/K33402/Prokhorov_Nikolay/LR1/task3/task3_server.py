import argparse
import json
import socket
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body


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
    def query(self) -> dict:
        return parse_qs(self.url.query)

    @property
    @lru_cache(maxsize=None)
    def url(self):
        return urlparse(self.target)


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
    MAX_HEADERS = 100
    MAX_LINE = 64 * 1024

    def __init__(self, host, port, server_name):
        self._marks = {
            "Student #5": {
                "WEB программирование": 64,
                "Frontend разработка":  97,
                "Операционные системы": 82,
                "Физика":               77
            }
        }

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

            print(f'Сервер запущен по адресу {self._host}:{self._port}')

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
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
        except Exception as e:
            self.send_error(conn, e)

        if conn:
            conn.close()

    def parse_request_line(self, rfile):
        raw = rfile.readline(self.MAX_LINE + 1)
        if len(raw) > self.MAX_LINE:
            raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()
        if len(words) != 3:
            raise Exception('Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        return words

    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')
        if host not in (self._server_name,
                        f'{self._server_name}:{self._port}'):
            raise Exception('Not found')
        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(self.MAX_LINE + 1)
            if len(line) > self.MAX_LINE:
                raise Exception('Header line is too long')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > self.MAX_HEADERS:
                raise Exception('Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def handle_request(self, req: Request) -> Response:
        if req.path == '/marks' and req.method == 'POST':
            return self.handle_post_marks(req)

        if req.path == '/marks' and req.method == 'GET':
            return self.handle_get_marks(req)

        raise Exception('Not found')

    def handle_get_marks(self, req: Request) -> Response:
        accept = req.headers.get('Accept')
        if 'text/html' in accept:
            content_type = 'text/html; charset=utf-8'
            body = '<html><head><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-uWxY/CJNBR+1zjPWmfnSnVxwRheevXITnMqoEIeG1LJrdI0GlVs/9cVSyPYXdcSF" crossorigin="anonymous"></head><body>'

            body += '<div class="container">'
            body += '<div class="text-center mt-3">'
            body += '<h1>Оценки студентов по дисциплинам</h1>'
            body += f'<p>Студентов в базе: {len(self._marks)}</p>'
            body += '</div>'

            body += '<div class="container"><table class="table table-striped table-hover">'
            body += '<thead> <tr> <th scope="col">Студент</th> <th scope="col">Дисциплина</th> <th scope="col">Оценка</th> </tr> </thead>'
            body += '<tbody>'

            for student in self._marks:
                if len(self._marks[student]) != 0:
                    for discipline in self._marks[student]:
                        body += '<tr>'
                        body += f'<td>{student}</td>'
                        body += f'<td>{discipline}</td>'
                        body += f'<td>{self._marks[student][discipline]}</td>'
                        body += '</tr>'

            body += '</tbody>'
            body += '</table></div>'

            body += '</body></html>'

        elif 'application/json' in accept:
            content_type = 'application/json; charset=utf-8'
            body = json.dumps(self._marks)

        else:
            return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post_marks(self, request: Request) -> Response:
        student = request.query['student'][0]
        discipline = request.query['discipline'][0]
        mark = request.query['mark'][0]

        if student not in self._marks:
            self._marks[student] = {}

        if discipline not in self._marks[student]:
            self._marks[student][discipline] = {}

        self._marks[student][discipline] = mark

        return Response(204, 'Created')

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

    def send_error(self, conn, err: HTTPError):
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
    parser = argparse.ArgumentParser(description='Сервер для задачи №3')
    parser.add_argument('--name', help='Хостовое имя сервера', default='localhost')
    parser.add_argument('--host', help='IP хоста', default='localhost')
    parser.add_argument('--port', help='Порт хоста', default=8888)

    args = parser.parse_args()

    server = MyHTTPServer(args.host, args.port, args.name)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
