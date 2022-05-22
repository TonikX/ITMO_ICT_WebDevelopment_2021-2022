import socket

if __name__ == "__main__":
    sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(3)]
    [sock.connect(("127.0.0.1", 8000)) for sock in sockets]

    user1, user2, user3 = sockets

    user1.send(b"room_id=1&message=hello, world! I'm user 1!")
    print(user1.recv(1024))
    user2.send(b"room_id=1&message=hello, world! I'm user 2!")
    print(user1.recv(1024))
    user3.send(b"room_id=1&message=hello, world! I'm user 3!")
    print(user1.recv(1024))
    print(user2.recv(1024))

    user1.close()
    user2.close()
    user3.close()
