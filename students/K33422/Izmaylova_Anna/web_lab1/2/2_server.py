import socket # библиотека для приема/передачи данных

sock = socket.socket() # создание сокета (комбинация IP и номера порта)
sock.bind(('127.0.0.1', 9091)) 
sock.listen(1) # сколько клиентов готов слушать сервер
connection, addr = sock.accept() # принимаем подключение

# print('connected:', addr)

data = connection.recv(1024) # Получение данных от клиента
data = data.decode() # превратить байты в строку
# print(data) 
lst = data.split(" ") # список запроса
url = lst[1] # взять из списка только адрес с параметрами
url_lst = url.split("?") # ['https://localhost', 'a=23&b=34&c=56']
params = url_lst[1] # 'a=23&b=34&c=56'
params_lst = params.split("&") # ['a=45', 'b=67', 'c=34']
params_lst[0] = params_lst[0].split("=")[1] # 'a=45' -> '45'
params_lst[1] = params_lst[1].split("=")[1] # 'b=67' -> '67'
params_lst[2] = params_lst[2].split("=")[1] # 'c=34' -> '34'
a = int(params_lst[0]) # '45' -> 45 
b = int(params_lst[1]) # '67' -> 67
c = int(params_lst[2])

# решение квадратного уравнения
discr = b ** 2 - 4 * a * c
 
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    answer = f"x1 = {x1} \nx2 = {x2}"
    connection.send(answer.encode())
elif discr == 0:
    x = -b / (2 * a)
    answer = f"x = {x}"
    connection.send(answer.encode())
else:
    connection.send("Корней нет".encode()) 


connection.close() # Закроем подключение