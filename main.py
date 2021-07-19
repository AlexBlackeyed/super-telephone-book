from os import name, system
import time
import colorama
from colorama import Fore
from colorama import Style
import shutil
import requests
from datetime import datetime


def centered(s):
    print(s.center(shutil.get_terminal_size().columns))


#just a cool looking ascii 
def logo():
	centered("SUPER TELEPHONE BOOK")
	centered('''
	░██████╗████████╗██████╗░
	██╔════╝╚══██╔══╝██╔══██╗
	╚█████╗░░░░██║░░░██████╦╝
	░╚═══██╗░░░██║░░░██╔══██╗
	██████╔╝░░░██║░░░██████╦╝
	╚═════╝░░░░╚═╝░░░╚═════╝
	''')


	
def welcome_text():
	time.sleep(2)
	print("Welcome To The Super Telephone Book\n What do you want to do next?")





def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')


def option_one():	
	while True:
		first_name = input("What's your First Name? : ")
		if first_name.isalpha():
			break
		else:
			continue 
	while True:
		surname = input("What's your Surname? : ")
		if surname.isalpha():
			break
		else:
			continue
	while True:
		telephone_number = input("What's your Telephone Number? : ")
		if telephone_number.isalpha():
			continue
		else:
			break
	while True:
		location = input("In which City do you live in? : ")
		if  location.isdigit():
			continue
		else:
			break
	adress = input("What's your Adress? : ")
	while True:
		zip_code = input("What's your Zip Code? : ")
		if zip_code.isalpha():
			continue
		else:
			break		
	while True:
		email_address = input("Input your email adress : ")
		response = requests.get(
			"https://isitarealemail.com/api/email/validate",
			params = {'email': email_address})

		status = response.json()['status']
		if status == "valid":
			break
		elif status == "invalid":
			print("email is invalid")
			continue
		else:
			print("email was unknown")
			continue
	
	while True:
		birthday = input("When were you born? : ")
		try:
			dt_start = datetime.strptime(birthday, '%d/%m/%Y')
			dt_start
			break
		except ValueError:
			print("Incorrect format. You should write it like this: dd/mm/yyyy")
			continue
	first_name.capitalize()
	surname.capitalize()
	location.capitalize()
	adress.capitalize()
	txt_name = first_name + "_" + surname
	data = first_name, surname, telephone_number, location, adress, zip_code, email_address, birthday
	data = list(data)
	basic_info = first_name + " " + surname
	with open(''+txt_name+'.txt', "w+") as sh:
		for i in data:
			sh.write(i)
			sh.write("\n")
	with open("names.txt", "w+") as main_catalog:
		main_catalog.write("\n")
		main_catalog.write('\n')
		main_catalog.write(basic_info)
		main_catalog.write("\n")
		main_catalog.write(telephone_number)
		

		

def find_contact():
	# opens file in read mode
	fh = open("names.txt", "r")
	# requests input from the user
	word = input("Input the contact you wish to find!\n >")
	s = " "
	count = 1
	# reads the txt file and tries to match the input with it
	while(s):
		s = fh.readline()
		L = s.split()
		if word in L:
			print("Line Number:", count, ":", s)
		
		count += 1
			

def delete_contact():
	# open file in read mode
	with open("super-telephone-book\\names.txt", "r") as f:						
		# read data line by line 
		dataa = f.readlines()
	# open file in write mode
	with open("super-telephone-book\\names.txt", "w") as f:
		for line in dataa :							
			# condition for data to be deleted
			if line.strip("\n") != delete_input : 
								f.write(line)				
					
				


def if_four():
	# opens txt file in read mode
	fo = open("super-telephone-book\\names.txt", 'r')
	#reads the txt
	contact_list=fo.read()
	#prints everything that is written in the txt file
	print(contact_list)
	print('\n')




def menu():
	colorama.init()
	print(Fore.MAGENTA + Style.DIM + "(01)" + Style.RESET_ALL + "Add new contact")
	print(Fore.MAGENTA + Style.DIM + "(02)" + Style.RESET_ALL + "Search for contact")
	print(Fore.MAGENTA + Style.DIM + "(03)" + Style.RESET_ALL + "Delete contact")
	print(Fore.MAGENTA + Style.DIM + "(04)" + Style.RESET_ALL + "Contact List")
	print(Fore.MAGENTA + Style.DIM + "(99)" + Style.RESET_ALL + "Exit")


def main_main_process():
	menu()
	while True:
		answer = int(input("Enter your option:"))
		if answer == 1:
			clear()
			logo()
			option_one()
			menu()			
		elif answer == 2:
			clear()
			logo()
			find_contact()
			menu()
		elif answer == 3:
				clear()
				logo()
				if_four()
				global delete_input
				delete_input = input("Input the contact from the ones above that you want to be deleted!\n Note. Copy and paste exactly the contact otherwise it wont work :D\n >")
				delete_contact()
				menu()	
		elif answer == 4:			
				if_four()
				menu()	
		else:
			clear()
			logo()
			print("Input a number given in the options:")
			menu()
		if answer == 99:
			clear()
			logo()
			print("Thanks for using this program.")
			time.sleep(2)
			quit()		

logo()
welcome_text()
main_main_process()