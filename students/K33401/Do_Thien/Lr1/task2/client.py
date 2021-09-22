import socket
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.connect((socket.gethostname(), 14900))

serversocket.send(b"Hello server! \n")
data = serversocket.recv(1024)
print("Server: " + data.decode("utf-8"))


print("Enter the lenghts of the side of the trapezoid!")
print("(Form: Top_edge Bottom_edge High_line)")
trapezoid = list(map(int, input("Input: ").strip().split()))[:3]

data_trapezoid = pickle.dumps(trapezoid)
serversocket.send(data_trapezoid)
data_area = serversocket.recv(1024)
area = pickle.loads(data_area)
print("The area of the trapezoid: " + str(area))
serversocket.close()
