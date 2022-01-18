import socket
import threading

class Server:
	def __init__(self, host: str, port: int):
		self.host = host
		self.port = port 
		self.users = []
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))
		self.sock.listen(10)

	def listen_client(self, client_socket: socket.socket):
		client_socket.settimeout(60)
		while True:
			try:
				data = client_socket.recv(1024)
				for cliento in self.users.copy():
					if cliento != client_socket:
						cliento.send(data)
			except KeyboardInterrupt:
				self.sock.close()


	def run(self):
		while True:
			try:
				client_socket, address = self.sock.accept()
				print(f"Address {address} connected")
				if client_socket not in self.users:
					self.users.append(client_socket)
				thread = threading.Thread(target=self.listen_client, args=(client_socket,))
				thread.start()
			except KeyboardInterrupt:
				self.sock.close()
				break

if __name__ == '__main__':
	host = "localhost"
	port = 14900
	print("Launching in 3..2..1")
	server = Server(host, port)
	thread1 = threading.Thread(target=server.run)
	thread1.start()