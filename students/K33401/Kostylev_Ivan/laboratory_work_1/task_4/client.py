import socket
import sys
import time

def run_client(host, port, user_name):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((host, port))
    while True:
        try:
            hello_server = f"{user_name} > Hello, Server!"
            conn.send(hello_server.encode("utf-8"))
        except KeyboardInterrupt:
            conn.close()
        
        time.sleep(2)

if __name__=='__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    user_name = sys.argv[3]
    run_client(host, port, user_name)