import socket
import time

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 14900))
conn.listen(1)
conn.setblocking(False)

while True:
    try:
        client_s, address = conn.accept()
        print(f"Connected to: {address}")
        conn.setblocking(True)
        data = client_s.recv(16384)
        data = data.decode("utf-8")
        print(("Data received: " + data))
        server_message = "Hello, client!"
        client_s.send(bytes(server_message, "utf-8"))
        conn.close()
    except socket.error:
        time.sleep(5)
    except KeyboardInterrupt:
        conn.close()
        break