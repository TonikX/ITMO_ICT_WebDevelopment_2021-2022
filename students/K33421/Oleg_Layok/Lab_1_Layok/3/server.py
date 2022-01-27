import socket

connection = socket.socket()
host = "127.0.0.1"
port = 5000
connection.bind((host, port))
connection.listen()

exit = False

while not exit:
    try:
        client, (client_host, client_port) = connection.accept()
        print("Connected to", client_host, client_port)
        responce_type = "HTTP/1.0 200 OK\n"
        headers = 'Connect-Type: text/html\n\n'
        page = open('index.html', 'r')
        body = ''.join(page)
        responce = responce_type + headers + body
        client.send(responce.encode('utf-8'))
        client.close()
    except KeyboardInterrupt:
        exit = True
        print("Stop")

connection.close()