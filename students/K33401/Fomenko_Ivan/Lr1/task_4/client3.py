from client import Client, welcome

if __name__ == '__main__':
	host = "localhost"
	port = 14900
	username = welcome()
	client = Client(host, port, username)
	client.run()