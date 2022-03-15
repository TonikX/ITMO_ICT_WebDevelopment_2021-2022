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
        self._marks = {}

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
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<div>Оценки группы по дисциплине (в базе студентов: {len(self._marks)})</div>'
            body += '<ul>'
            for student in self._marks:
                body += '<li>'
                body += student
                body += '<ul>'
                for task in self._marks[student]:
                    body += f'<li>{task}: {self._marks[student][task]}</li>'
                body += '</ul>'
                body += '</li>'
            body += '</ul>'
            body += '</body></html>'

        elif 'application/json' in accept:
            contentType = 'application/json; charset=utf-8'
            body = json.dumps(self._marks)

        else:
            return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', contentType),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post_marks(self, req: Request) -> Response:
        student = req.query['student'][0]
        task = req.query['task'][0]
        mark = req.query['mark'][0]

        if student not in self._marks:
            self._marks[student] = {}
        if task not in self._marks[student]:
            self._marks[student][task] = {}
        self._marks[student][task] = mark

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
    parser = argparse.ArgumentParser(description='Task 3 Server')
    parser.add_argument('--name', help='Host of the server', default='127.0.0.1')
    parser.add_argument('--host', help='Hostname/IP to bind', default='127.0.0.1')
    parser.add_argument('--port', help='Port to bind', default=1337)
    parser.add_argument('-b', '--buffer', help='Connection buffer size', type=int, default=1024)
    args = parser.parse_args()

    server = MyHTTPServer(args.host, args.port, args.name)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
