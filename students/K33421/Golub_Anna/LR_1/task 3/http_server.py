import socket
import sys
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._marks = dict()

    def serve_forever(self):
        # print('serve_forever')

        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            proto=0)

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                # print('start while')
                conn, _ = serv_sock.accept()
                # print(conn)
                try:
                    self.serve_client(conn)
                    # print('back in serve_forever')
                    # print(conn)
                except Exception as e:
                    print('Client serving failed:', e)
                # print('while done')
        finally:
            serv_sock.close()

    def serve_client(self, conn):
        # print('serve_client')
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
            # raise ConnectionResetError
        except Exception as e:
            # raise e
            self.send_error(conn, e)
        if conn:
            conn.close()
        # print('serve_client done')

    def parse_request(self, conn):
        # print('parse_request')
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        # print('parse_headers')
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')
            if line in (b'\r\n', b'\n', b''):  # завершаем чтение заголовков
                break
            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise Exception('Too many headers')

        headers_dict = dict()
        for h in headers:
            h = h.decode('iso-8859-1')
            k, v = h.split(':', 1)
            headers_dict[k] = v
        return headers_dict

    def parse_request_line(self, rfile):
        # print('parse_request_line')
        raw = rfile.readline(MAX_LINE + 1)  # эффективно читаем строку целиком
        if len(raw) > MAX_LINE:
            raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()  # разделяем по пробелу
        if len(words) != 3:  # и ожидаем ровно 3 части
            raise Exception('Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')
        return method, target, ver

    def handle_request(self, req):
        # print('handle_request')
        if req.path == '/marks' and req.method == 'POST':
            subject = req.query['subject'][0]
            mark = req.query['mark'][0]
            if subject in self._marks:
                self._marks[subject].append(mark)
            else:
                self._marks[subject] = [mark]
            return Response(204, 'Created')

        if req.path == '/marks' and req.method == 'GET':
            subject = req.query['subject'][0]
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'Subject: <b>{subject}</b><br>'
            if subject in self._marks:
                body += f'Marks: {", ".join(self._marks[subject])}'
            else:
                body += f'Marks: no data'
            body += '</body></html>'
            body = body.encode('utf-8')
            headers = [('Content-Type', contentType), ('Content-Length', len(body))]
            return Response(200, 'OK', headers, body)

        raise HTTPError(404, 'Not found')

    def send_response(self, conn, resp):
        # print('send_response')
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
        # print('send_error')
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
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]

    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
