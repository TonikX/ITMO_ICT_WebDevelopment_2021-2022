import socket
import re

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 4341))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384).decode("utf-8")
        helping_list = (re.findall(r'\d+', data))
        helping_num = list(map(int, helping_list))
        a, b, h = helping_num
        s = 0.5 * (a + b) * h
        clientsocket.send(str(s).encode())
    except KeyboardInterrupt:
        conn.close()
        break
