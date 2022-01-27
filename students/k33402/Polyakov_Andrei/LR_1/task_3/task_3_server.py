import socket
import sys


class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.bind((self.host, self.port))
        conn.listen(10)
        while True:
            clientsocket, address = conn.accept()
            self.serve_client(clientsocket)

    def serve_client(self, clientsocket):
        data = clientsocket.recv(16384)
        data = data.decode('utf-8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp:
            self.send_response(clientsocket, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        i = lines.index('')
        headers = lines[1:i]
        body = lines[-1]
        return url, method, headers, body

    def handle_request(self, url, method, body):
        if url == "/":
            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html', 'r') as f:
                    resp += f.read()
                return resp
            if method == "POST":

                newbody = body.split('&')
                for a in newbody:
                    if a.split('=')[0] == 'subject':
                        subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        marks.append(a.split('=')[1])

                resp = "HTTP/1.1 200 OK\n\n"
                resp += "<html><head><title>Journal</title></head><body><table border=1>"
                for s, m in zip(subjects, marks):
                    resp += f"<tr><td>{s}</td><td>{m}</td></tr>"
                resp += "</table></body></html>"
                return resp

    def send_response(self, clientsocket, resp):
        clientsocket.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    serv = MyHTTPServer(host, port)
    subjects = []
    marks = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass