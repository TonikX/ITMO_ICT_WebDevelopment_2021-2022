import socket
import pickle

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(4096)
    data_variable = pickle.loads(data)
    if not data:
        break
    print('a = ', data_variable['a'])
    print('b = ', data_variable['b'])
    print('h = ', data_variable['h'])
    summ = str(int(data_variable['h'])*(int(data_variable['a'])+int(data_variable['b']))/2)

    conn.send(summ.encode())

conn.close()