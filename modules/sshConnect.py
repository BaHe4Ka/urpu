import paramiko

def connect():
	psw = input("Please, enter your current router admin panel password: ")
	host = "192.168.1.1"
	port = 22

	print("Trying to connect, please, wait...")

	
	try:	

		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname = host, username = "root", password = psw, port = port)
		print("Connected succesfuly")
		return client
		
	except:

		print("We`re expierenciing technical difficulties")

		return None
