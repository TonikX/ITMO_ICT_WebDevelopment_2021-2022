import socket
import sys
from functools import lru_cache
from urllib.parse import parse_qs, urlparse
import json

MAX_LINE = 64 * 1024
MAX_HEADERS = 100

class MyHTTPServer:

    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._data = dict()
  

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((self._host, self._port))
            sock.listen()
            while True:
                conn, _ = sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print("Client serving failed with exception", e)
        finally:
            sock.close()


    def serve_client(self, connection):
        try:
            request = self.parse_request(connection)
            response = self.handle_request(request)
            self.send_response(connection, response)
        except ConnectionResetError as e:
            connection = None
        except Exception as e:
            connection = None


    def parse_request(self, connection):
        rfile = connection.makefile('rb')
        method, url, version = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        return Request(method, url, version, rfile)


    def parse_request_line(self, rfile):
        line = rfile.readline(MAX_LINE + 1)
        if len(line) > MAX_LINE:
            raise Exception('Request line is too long')
        req_line = str(line, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()     
        if len(words) != 3:
            raise Exception('Malformed request line')
        method, url, version = words
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')
        return (method, url, version)
    

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
        return headers


    def handle_request(self, req):
        if req.method == 'POST':
            return self.handle_post(req)
        if req.method == 'GET':
            return self.handle_get(req)
        return Response(400, 'Bad request')


    def handle_post(self, req):
        self._data = req.query
        return Response(204, 'Created')

    def handle_get(self, req):
        accept = req.headers.get('Accept')
        if 'application/json' in accept:
            contentType = 'application/json; charset=utf-8'
            body = json.dumps(self._data)
        else:
            return Response(406, 'Not Acceptable')
        body = body.encode('utf-8')
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


class Request:
    def __init__(self, method, target, version, rfile):
        self.method = method
        self.target = target
        self.version = version
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
        

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]

    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass