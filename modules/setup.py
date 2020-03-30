import json, os

dirToProfiles = "./profiles/"
ignoreList = ["Translations.json"]
translationsFile = dirToProfiles + "Translations.json"
with open(translationsFile) as f:
		translations = json.load(f)

def menu():
	print("Please, select a profile:")
	profilesList = os.listdir(dirToProfiles)
	
	while (ignoreList):
		repeat = False
		for i in range(len(profilesList)):
			for j in range(len(ignoreList)):
				#print(profilesList[i], ignoreList[j])
				if (profilesList[i] == ignoreList[j]):
					profilesList.pop(i)
					ignoreList.pop(j)
					repeat = True
					break
			if (repeat): break
		if (not repeat): break 

	for i in range(len(profilesList)):
		print(str(i + 1) + ") " + profilesList[i][:-5])
	choise = int(input())

	return(start(dirToProfiles + profilesList[choise - 1]))

def start(file):
	with open(file) as f:
		settings = json.load(f)

	values = list()

	for var, val in settings.items():
		if (val != "Custom"): values.append([var, val])
		else: 
			value = input(translations[var])
			values.append([var, value])

	return values