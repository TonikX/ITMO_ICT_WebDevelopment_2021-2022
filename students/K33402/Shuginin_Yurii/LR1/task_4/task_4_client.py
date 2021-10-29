import socket
import threading
import time

def get_msgs():
    while not exit_event.is_set():
        try:
            msg = conn.recv(16384).decode("utf-8")
            print(msg)
        except socket.error:
            time.sleep(0.25)
            continue


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 9090))
conn.setblocking(False)
print("Connecting to the Chat")

exit_event = threading.Event()
get_thread = threading.Thread(target=get_msgs)
get_thread.start()

try:
    while True:
        message = input()
        if message:
            conn.send(message.encode())

except KeyboardInterrupt:
    print("\n" + "Disconnecting" + "\n")

    exit_event.set()
    get_thread.join()
    
    conn.close()
