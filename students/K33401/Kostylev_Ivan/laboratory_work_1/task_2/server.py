import socket
import math
from typing import cast

HOST, PORT = "127.0.0.1", 14900

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind((HOST, PORT))
conn.listen(5)

try: 
    sock, address = conn.accept()
    client_data = sock.recv(16384)
    client_data = client_data.decode("utf-8")
    print("Calculating Pifagor for data: " + client_data)
    a, b = [float(num) for num in client_data.split(" ")]
    res = math.sqrt(a ** 2 + b ** 2)
    msg_for_client = str(res)
    sock.send(msg_for_client.encode("utf-8"))
    conn.close()
except:
    print("except")
    conn.close()