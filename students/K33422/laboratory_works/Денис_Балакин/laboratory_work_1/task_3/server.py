import json
from socket import *
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._lessons = {}

    def serve_forever(self):
        server = socket(AF_INET, SOCK_STREAM)

        try:
            server.bind((self._host, self._port))
            server.listen()

            while True:
                connection, _ = server.accept()
                try:
                    self.serve_client(connection)
                except Exception as e:
                    print("Client serving failed", e)
        finally:
            server.close()

    def serve_client(self, connection):
        try:
            request = self.parse_request(connection)
            response = self.handle_request(request)
            self.send_response(connection, response)
        except ConnectionResetError:
            connection = None
        except Exception as e:
            self.send_error(connection, e)

    def parse_request(self, connection):
        rfile = connection.makefile('rb')
        method, target, version = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise HTTPError(400, 'Bad request', 'Host header is missing')

        if host not in (self._server_name, f'{self._server_name}:{self._port}'):
            raise HTTPError(404, 'Not found')

        return Request(method, target, version, headers, rfile)

    def parse_request_line(self, rfile):
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request', 'Request line is too long')

        request_line = str(raw, 'iso-8859-1')
        words = request_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request', 'Malformed request line')

        method, target, ver = words

        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return method, target, ver

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise HTTPError(494, 'Request header too large')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise HTTPError(494, 'Too many headers')

        decoded_headers = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(decoded_headers)

    def handle_request(self, request):
        if request.path == '/lessons' and request.method == 'POST':
            return self.handle_post_lessons(request)

        if request.path == '/lessons' and request.method == 'GET':
            return self.handle_get_lessons(request)

        raise HTTPError(404, 'Not found')

    def handle_post_lessons(self, request):
        self._lessons[request.query['name'][0]] = request.query['mark'][0]

        return Response(204, 'Updated')

    def handle_get_lessons(self, request):
        accept = request.headers.get('Accept')
        if 'text/html' in accept:
            content_type = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<div>Предметы ({len(self._lessons)})</div>'
            body += '<ul>'
            for lessons_name in self._lessons.keys():
                body += f'<li>{lessons_name}: {self._lessons[lessons_name]}</li>'
            body += '</ul>'
            body += '</body></html>'

        elif 'application/json' in accept:
            content_type = 'application/json; charset=utf-8'
            body = json.dumps(self._lessons)

        else:
            return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type), ('Content-Length', len(body))]

        return Response(200, 'OK', headers, body)

    def send_response(self, connection, response):
        wfile = connection.makefile('wb')
        status_line = f'HTTP/1.1 {response.status} {response.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if response.headers:
            for (key, value) in response.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if response.body:
            wfile.write(response.body)

        wfile.flush()
        wfile.close()

    def send_error(self, connection, error):
        try:
            status = error.status
            reason = error.reason
            body = (error.body or error.reason).encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
            resp = Response(status, reason, [('Content-Length', len(body))], body)
            self.send_response(connection, resp)


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

    def body(self):
        size = self.headers.get('Content-Length')
        if not size:
            return None
        return self.rfile.read(size)


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 14900
    name = "server.local"
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass