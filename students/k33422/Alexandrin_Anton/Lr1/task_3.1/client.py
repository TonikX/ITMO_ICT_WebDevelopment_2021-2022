import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect('127.0.0.1', 5002)

request =
conn.send()