import random
import socket
import time

s = socket.socket()         # Create a socket object
host = "127.0.0.1"     # Get local machine name
port = 9085
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

while True:
    # Establish connection with client.    
    c, (client_host, client_port) = s.accept()
    print(client_host)
    c.send('HTTP/1.0 200 OK\n'.encode('utf-8'))
    c.send('Content-Type: text/html\n'.encode('utf-8'))
    c.send('\n'.encode('utf-8')) # header and body should be separated by additional newline
    c.send("""
        <html>
        <body>
        <h1>Hello World</h1> this is my server!
        </body>
        </html>
    """.encode('utf-8')) # Use triple-quote string.
    c.close()