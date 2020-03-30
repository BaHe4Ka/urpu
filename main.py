from modules import sshConnect, setup
	
	
def welcome():
	logo = list()
	logo.append("██╗   ██╗██████╗ ██████╗ ██╗   ██╗")
	logo.append("██║   ██║██╔══██╗██╔══██╗██║   ██║")
	logo.append("██║   ██║██████╔╝██████╔╝██║   ██║")
	logo.append("██║   ██║██╔══██╗██╔═══╝ ██║   ██║")
	logo.append("╚██████╔╝██║  ██║██║     ╚██████╔╝")
	logo.append(" ╚═════╝ ╚═╝  ╚═╝╚═╝      ╚═════╝ ")
	
	print()
	for i in range(len(logo)): print(logo[i])
	print("Ultimate Router Protection Utility v0.3.4b")
	menu()
	
def setupMyRouter():
	client = sshConnect.connect()

	if (client != None): 
		settings = setup.menu()
		for i in range(len(settings)):
			print("nvram set " + settings[i][0] + '="' + settings[i][1] + '"')
			client.exec_command("nvram set " + settings[i][0] + '="' + settings[i][1] + '"')
		client.exec_command("nvram commit")
		client.exec_command("reboot")

	try: 
		client.close()
	except: 
		pass
	
	menu()
	
def menu():
	print("1) Setup my Router!")
	print("2) Exit")
	res = input()
	
	if (res == "1"): setupMyRouter()
	elif (res == "2"): exit(0) 
	else: print("Please, type a vaild option")
	menu()
	
welcome()