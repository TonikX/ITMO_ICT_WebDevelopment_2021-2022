import socket
import time
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("localhost", 8080))
conn.listen(1)

clientsocket, address = conn.accept()
data = clientsocket.recv(22222)
count = (data.decode("utf-8")).split(' ')
with open("index.html", "w") as file:
    file.write("<!DOCTYPE html> \n<html> \n<body> \n")

    for i in range (0, len(count) - 1, 2):
        file.write("<h2>" +'Дисциплина: ' + count[i] +'   Баллы: ' + count[i+1] + "</h2>\n")
    file.write("\n</html> \n</body> \n")

page = open('index.html')
answer = page.read()
page.close()
response_type = 'HTTP/1.0 200 OK\n'
headers = 'Content-Type: text/html\n'
response = response_type + headers + answer
data = response.encode("utf-8")

clientsocket.sendall(data)
time.sleep(15)
conn.close()
#for i in range(count):
#    clientsocket.send(str.encode('Введите ' + '%(i+1)' + ' дисциплину и количество баллов \n'))
#page = open('index.html')
#answer = page.read()
#page.close()
#response = 'HTTP/1.0 200 OK\n' + answer
#clientsocket.sendall(response.encode())
'''headers = [
    'GET / HTTP/1.1',
    'Host: localhost',
    'Connection: keep:alive',
    'Accept: index.html'
    '\n'
]
content = '\n'.join(headers)
print(content)
conn.send(content.encode())'''


