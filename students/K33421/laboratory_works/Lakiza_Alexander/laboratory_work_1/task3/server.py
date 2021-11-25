import socket
import re


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.journal = {}

    def serve_forever(self):
        # Starting a server on a socket, handling connections
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.bind((self.host, self.port))
        conn.listen(10)
        while True:
            clientsocket, address = conn.accept()
            self.serve_client(clientsocket)

    def serve_client(self, clientsocket):
        data = clientsocket.recv(16384)
        data = data.decode('utf-8')
        url, method, headers = self.parse_request(data)
        resp = self.handle_request(url, method)
        if resp:
            self.send_response(clientsocket, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        i = lines.index('')
        headers = lines[1:i]
        print(url)
        return url, method, headers

    def handle_request(self, url, method):
        if url == '/subjects/':
            resp = "HTTP/1.1 200 OK\n\n"
            with open('index.html', 'w') as f:
                text = '<!DOCTYPE html><html lang="en"><head><html><head><title>Journal</title></head></html><body>'
                for i in self.journal:
                    text += f"<b>{i}</b> : {self.journal[i]}</br></body></html>"
                f.write(text)
            resp += text
            return resp
        if method == 'GET':
            resp = "HTTP/1.1 200 OK\n\n"
            subject = re.findall('\?(.*)$', url)[0]
            subject = subject.split('=')[1]
            with open('index.html', 'w') as f:
                text = '<!DOCTYPE html><html lang="en"><head><html><head><title>Journal</title></head></html><body>'
                if subject in self.journal:
                    text += f"<b>{subject}</b> : {self.journal[subject]}</br></body></html>"
                else:
                    text += f"There is no <b>{subject}</b> in the journal</body></html>"
                f.write(text)
            resp += text
            return resp
        else:
            resp = "HTTP/1.1 200 OK\n\n"
            info = re.findall('\?(.*)$', url)[0]
            info = info.split('&')
            subject = info[0].split('=')[1]
            grade = info[1].split('=')[1]
            self.journal[subject] = grade
            with open('index.html', 'w') as f:
                text = '<!DOCTYPE html><html lang="en"><head><html><head><title>Journal</title></head></html><body>'
                for i in self.journal:
                    print(self.journal)
                    text += f"<b>{i}</b> : {self.journal[i]}</br></body></html>"
                f.write(text)
            resp += f'<!DOCTYPE html><html lang="en"><head><html><head><title>Journal</title>' \
                    f'</head><body><b>{subject}</b> successfully added</body></html>'
            return resp

    def send_response(self, clientsocket, resp):
        clientsocket.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 5000
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
