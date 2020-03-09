from modules import sshConnect

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
	print("Ultimate Router Protection Utility v0.0.7a")
	menu()

def menu():
	res = input("1) Setup my Router!\n")
	if (res == "1"): sshConnect.connect()
	else: print("Please, type a vaild option")
	menu()

welcome()