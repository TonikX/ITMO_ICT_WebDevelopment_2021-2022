import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 5000))

a, b, c = input('enter the a, b, c values: ').split()
if not a:
    print('Invalid a value')
    conn.close()

values_dict = f'[{a}, {b}, {c}]'
conn.send(bytes(values_dict, 'utf-8'))

data = conn.recv(4096)
udata = data.decode('utf-8')
print(udata)

conn.close()
