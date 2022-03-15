import socket
import threading

def welcome():
	print("Nice to see you! Enter your nickname: ")
	nickname = input()
	print(f"{nickname} burst into the party")
	return nickname

class Client:
	def __init__(self, host: str, port: int, username: str):
		self.host = host
		self.port = port 
		self.username = username
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def get_message(self):
		while True:
			try:
				data = self.sock.recv(1024)
				udata = data.decode("utf-8")
				print(udata)
			except KeyboardInterrupt:
				self.sock.close()

	def send_message(self):
		while True:
			try:
				data = input()
				self.sock.send(f"{self.username} says: {data}".encode())
			except KeyboardInterrupt:
				self.sock.close()

	def run(self):
		self.sock.connect((self.host, self.port))
		thread2, thread1 = threading.Thread(target=self.get_message), threading.Thread(target=self.send_message)
		thread1.start()
		thread2.start()

