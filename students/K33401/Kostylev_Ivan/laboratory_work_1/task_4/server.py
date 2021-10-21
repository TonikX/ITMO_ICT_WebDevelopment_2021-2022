import threading
import socket
import time
import sys

def run_server(port=44346):
    serv_sock = create_serv_sock(port)
    cid = 0
    while True:
        client_sock = accept_client_conn(serv_sock, cid)
        t = threading.Thread(target=serve_client,
                            args=(client_sock, cid))
        t.start()
        cid += 1

def serve_client(client_sock, cid):
    while True:
        mes = client_sock.recv(100)
        data = mes.decode("utf-8")
        if data:
            print(data)

def create_serv_sock(serv_port):
    serv_sock = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM,
                                proto=0)
    serv_sock.bind(('', serv_port))
    serv_sock.listen()
    return serv_sock

def accept_client_conn(serv_sock, cid):
    client_sock, client_addr = serv_sock.accept()
    print(f'Client #{cid} connected '
          f'{client_addr[0]}:{client_addr[1]}')
    return client_sock

if __name__ == '__main__':
    try:
        port=int(sys.argv[1])
        run_server(port)
    except:
        run_server()