import socket


if __name__ == "__main__":
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("127.0.0.1", 8000))
    conn.send(b"Hello, Server")
    answer = conn.recv(16340)
    print(answer)
    conn.close()
