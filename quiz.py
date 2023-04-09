import json
import random


user = []

def luaj():
	print("\n==========KUIZI FILLON==========")
	piket = 0
	with open("asetet/questions.json", 'r+') as f:
		j = json.load(f)
		for i in range(10):
			no_of_questions = len(j)
			ch = random.randint(0, no_of_questions-1)
			print(f'\nP{i+1} {j[ch]["pyetja"]}\n')
			for option in j[ch]["opcionet"]:
				print(option)
			pergjigje = input("\nSheno pergjigjen tuaj: ")
			if j[ch]["pergjigje"][0] == pergjigje[0].upper():
				print("\nPergjigje e sakte")
				piket+=1
			else:
				print("\nPergjigje jo e sakte")
			del j[ch]
		print(f'\nREZULTATI FINAL: {piket}')

def pyetjet():
	if len(user) == 0:
		print("Per te shtuar pyetje duhet ne fillim te logoheni si ADMIN.")
	elif len(user) == 2:
		if user[1] == "ADMIN":
			print('\n==========SHTO PYETJE==========\n')
			ques = input("Shenoni pyetjen qe deshironi te shtoni:\n")
			opt = []
			print("Shenoni 4 opsionet me inicialet (A, B, C, D)")
			for _ in range(4):
				opt.append(input())
			ans = input("Sheno pergjigjen:\n")
			with open("asetet/questions.json", 'r+') as f:
				questions = json.load(f)
				pop = {"pyetja": ques, "opcionet": opt, "pergjigje": ans}
				questions.append(pop)
				f.seek(0)
				json.dump(questions, f)
				f.truncate()
				print("Pyetja u shtua me sukses.")		
		else:
			print("Nuk keni qasje per te shtuar pyetje. Vetem Admin-at mund te shtojne pyetje.")


def krijoLlogari():
	print("\n==========KRIJO LLOGARI==========")
	username = input("Shenoni emrin e perdoruesit: ")
	password = input('Shenoni fjalekalimin: ')
	with open('asetet/user_accounts.json', 'r+') as user_accounts:
		users = json.load(user_accounts)
		if username in users.keys():
			print("Kjo llogari ekziston.\nFutuni ne panelin e Login-it.")
		else:
			users[username] = [password, "PLAYER"]
			user_accounts.seek(0)
			json.dump(users, user_accounts)
			user_accounts.truncate()
			print("Llogaria juaj u krijua me sukses!")

def login():
	print('\n==========LOGIN==========')
	username = input("Shenoni emrin e perdoruesit: ")
	password = input('Shenoni fjalekalimin: ')
	with open('asetet/user_accounts.json', 'r') as user_accounts:
		users = json.load(user_accounts)
	if username not in users.keys():
		print("Logaria me kete emer nuk ekziston.\nKrijoni nje llogari te re.")
	elif username in users.keys():
		if users[username][0] != password :
			print("Fjalekalimi juaj eshte gabim.\nShenojeni perseri.")
		elif users[username][0] == password and users[username][1] == "ADMIN":
			print("Jeni kycur me sukses si admin.\n")
		elif users[username][0] == password and users[username][1] == "PLAYER":
			print("Jeni kycur me sukses si player.\n")

def logout():
	global user
	if len(user) == 0:
		print("Ju jeni i shkycur.")
	else:
		user = []
		print("ju jeni shkycur me sukses.")

def rregullat():
	print('''\n==========RREGULLAT==========
        1. Kuizi ka 10 pyetje te rastesishme. Per tu pergjigjur duhhet te zgjedhim njerin nga opsionet A-B-C-D te cilet nuk jan case sensitive qe dmth se mund te shenojme edhe a-b-c-d-.
        Piket tuaja totale do te shenohen ne fund te kuizit.
        
        2.Secila pyetje ka 1 pike. Nuk ka pike negative per pergjigjet e gabuara.
        
        3.Ju mund te krijoni nje llogari tuajen, tek paneli per krijim te llogaris.
        
        4.Ju mund te kyceni nepermjet panelit per kycje apo login. Momentalisht, programi ka vetem opsionin per login .
        
	''')

	

def rrethNesh():
	print('''\n==========RRETH NESH==========
Ky projekt eshte krijuar nga Sadri Sali dhe Arjan Shabani.''')

if __name__ == "__main__":
	zgjidhja = 1
	while zgjidhja != 7:
		print('\n=========MIRESEVINI NE KUIZ==========')
		print('-----------------------------------------')
		print('1. FILLO KUIZIN')
		print('2. SHTO PYETJE')
		print('3. KRIJO LLOGARI')
		print('4. KYCU(LOGIN)')
		print('5. SHKYCU(LOGOUT)')
		print('6. SHIKO UDHEZIMET RRETH LOJES')
		print('7. DALJE')
		print('8. RRETH NESH')
		zgjidhja = int(input('ZGJIDH NJEREN NGA OPSIONET: '))
		if zgjidhja == 1:
			luaj()
		elif zgjidhja == 2:
			pyetjet()
		elif zgjidhja == 3:
			krijoLlogari()
		elif zgjidhja == 4:
			login()
		elif zgjidhja == 5:
			logout()
		elif zgjidhja == 6:
			rregullat()
		elif zgjidhja == 7:
			break
		elif zgjidhja == 8:
			rrethNesh()
		else:
			print('GABIM! ZGJIDH NJE OPSION PERSERI.')
