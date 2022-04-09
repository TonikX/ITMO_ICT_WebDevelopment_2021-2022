#server

import json
import socket
import traceback
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_HEADERS = 100
MAX_LINE = 64 * 1024

class MyHTTPServer:
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name


    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0) 

        try:
            serv_sock.bind((self._host, self._port)) 
            serv_sock.listen() 

            print(f'http://{self._host}:{self._port}/index') 

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
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request',
                            'Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        words = req_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request',
                            'Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return words

    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')
        if host not in (self._host,
                        f'{self._host}:{self._port}'):
            raise Exception('Not found')
        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise Exception('Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def handle_request(self, req):
        if req.path == '/index' and req.method == 'POST':
            return self.handle_post(req)

        if req.path == '/index' and req.method == 'GET':
            return self.handle_get(req)

        raise Exception('Not found')

    def handle_get(self, req):
        accept = req.headers.get('Accept')
        if 'text/html' in accept:
            content_type = 'text/html; charset=utf-8'
            body = '<html><head><style>span {padding: 0px;}</style></head><body><h1>Hello, world!</h1></body></html>'

        elif 'application/json' in accept:
            content_type = 'application/json; charset=utf-8'
            body = json.dumps(self._grades)

        else:
            return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, request):
        discipline = request.query['discipline'][0]
        grade = request.query['grade'][0]

        if discipline not in self._grades:
            self._grades[discipline] = []

        self._grades[discipline].append(grade)

        return Response(200, 'OK')

    def send_response(self, conn, resp):
        rfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        rfile.write(status_line.encode('iso-8859-1'))

        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                rfile.write(header_line.encode('iso-8859-1'))

        rfile.write(b'\r\n')

        if resp.body:
            rfile.write(resp.body)

        rfile.flush()
        rfile.close()

    def send_error(self, conn, err):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except:
            status = 500
            traceback.print_exc()
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
        resp = Response(status, reason,
                        [('Content-Length', len(body))],
                        body)
        self.send_response(conn, resp)


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


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 10203
    name = "localhost"

    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
