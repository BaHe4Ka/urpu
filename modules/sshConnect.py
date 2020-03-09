import paramiko

def connect():
	lgn = input("Please, type your router login: ")
	psw = input("Please, type your router password: ")
	host = "192.168.1.1"
	port = 22

	
		
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname = host, username = "root", password = psw, port = port)
	client.exec_command('nvram set language="russian"')
	client.exec_command('nvram commit')
	client.close()
	print("Succesfuly changed language to RUSSIAN")
	
	#except:

	#	print("Unknown error!")
