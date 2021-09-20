import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip().decode()
        split_data = self.data.split()
        method = split_data[0]
        path = split_data[1]
        if method == "GET" and path == "/index.html":
            with open("index.html", "rb") as f:
                resp = f.read()
        else:
            resp = b"Unsupported request method or path\n"
        self.request.sendall(resp)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
