import socket


host, port = "127.0.0.1", 14900

conn = socket.socket()
conn.bind((host, port))


print("Starting server on", host, port)
print("The Web server URL for this would be http://%s:%d/" % (host, port))

conn.listen(10)

print("Entering infinite loop; hit CTRL-C to exit")

while True:
    client, (client_host, client_port) = conn.accept()
    print("Got connection from", client_host, client_port)
    client.recv(1000)
    response_type = "HTTP/1.0 200 OK\n"
    headers = "Content-Type: text/html\n\n"
    body = """
        <html>
        <body>
        <h1>Hello Client<h1>!
        </body>
        </html>
    """
    response = response_type + headers + body
    client.send(response.encode("utf-8"))
    client.close

