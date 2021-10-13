from os import name, system, remove, path
import time
from colorama import Fore, Style
import shutil
import requests
from datetime import datetime
import subprocess


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
		phone = input("What's your Telephone Number? (ex. +44........): ")
		api_key = '2dcce2ea93f947389bdb82eef26bd2d4'
		response_phone = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key={api_key}&phone={phone}")
		phone_data = response_phone.json()
		valid = response_phone.status_code
		if valid > 200:
			continue_input = input("Do you want to try again?[y/n]")
			if continue_input == 'y':
				continue
			else:
				break
		location = phone_data['location']
		break
		
		
	address = input("What's your Address? : ")
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
	first_name = first_name.capitalize()
	surname = surname.capitalize()
	location = location.capitalize()
	address = address.capitalize()
	txt_name = first_name + "_" + surname
	data = "First Name: " + first_name, "Surname: " +surname, "Telephone Number: " + phone, "Location: " + location, "Address: " +address, "Zip Code: " + zip_code, "Email Address: " +email_address, "Birthday: " + birthday
	data = list(data)
	basic_info = first_name + "_" + surname
	with open('super-telephone-book\\'+txt_name+'.txt', "w+") as sh:
		for i in data:
			sh.write(i)
			sh.write("\n")
	with open("super-telephone-book\\names.txt", "w+") as main_catalog:
		main_catalog.write("\n")
		main_catalog.write('\n')
		main_catalog.write(basic_info)
		

		

def find_contact():
	# opens file in read mode
	fh = open("super-telephone-book\\names.txt", "r")
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
	delete_path = 'super-telephone-book\\'+delete_input+'.txt'
	if path.exists(delete_path):
		remove(delete_path)
	else:
		print("The file does not exist")
			
					
				


def if_four():
	# opens txt file in read mode
	fo = open("super-telephone-book\\names.txt", 'r')
	#reads the txt
	contact_list=fo.read()
	#prints everything that is written in the txt file
	print(contact_list)
	print('\n')


def edit_contact():
	if_four()
	while True:
		edit_input = input("Input the contact that you want to edit: ")
		global edit_input_path
		edit_input_path = 'super-telephone-book\\'+edit_input+'.txt'
		if path.exists(edit_input_path):
			notepad_run()
			break
		else:
			print("Please input a valid contact")
			continue


	

	

def menu():
	print(Fore.MAGENTA + Style.DIM + "(01)" + Style.RESET_ALL + "Add new contact")
	print(Fore.MAGENTA + Style.DIM + "(02)" + Style.RESET_ALL + "Search for contact")
	print(Fore.MAGENTA + Style.DIM + "(03)" + Style.RESET_ALL + "Delete contact")
	print(Fore.MAGENTA + Style.DIM + "(04)" + Style.RESET_ALL + "Contact List")
	print(Fore.MAGENTA + Style.DIM + "(05)" + Style.RESET_ALL + "Edit Contact")
	print(Fore.MAGENTA + Style.DIM + "(99)" + Style.RESET_ALL + "Exit")


def cleanup():
	clear()
	logo()
def main_main_process():
	menu()
	while True:
		answer = int(input("Enter your option:"))
		if answer == 1:
			cleanup()
			option_one()
			menu()			
		elif answer == 2:
			cleanup()
			find_contact()
			menu()
		elif answer == 3:
				cleanup()
				if_four()
				global delete_input
				delete_input = input("Input the contact from the ones above that you want to be deleted!\n Note. Copy and paste exactly the contact otherwise it wont work :D\n >")
				delete_contact()
				menu()	
		elif answer == 4:
				cleanup()			
				if_four()
				menu()	
		elif answer == 5:
			cleanup()
			edit_contact()
		else:
			cleanup()
			print("Input a number given in the options:")
			menu()
		if answer == 99:
			cleanup()
			print("Thanks for using this program.")
			time.sleep(2)
			quit()		

def notepad_run():
	subprocess.run(["notepad", edit_input_path])


def main():
	logo()
	welcome_text()
	main_main_process()


main()