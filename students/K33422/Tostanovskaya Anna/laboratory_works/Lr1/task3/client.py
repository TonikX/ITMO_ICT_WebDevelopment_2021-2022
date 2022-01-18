import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 14900))
msg = sock.recv(16384)
print(msg.decode("utf-8"))
sock.close()