import os
from os import name, system
import time
import colorama
from colorama import Fore
from colorama import Style


print("                              SUPER TELEPHONE BOOK")
time.sleep(2)
#just a cool looking ascii 
def logo():
	print('''   
                            ░██████╗████████╗██████╗░
                            ██╔════╝╚══██╔══╝██╔══██╗
                            ╚█████╗░░░░██║░░░██████╦╝
                            ░╚═══██╗░░░██║░░░██╔══██╗
                            ██████╔╝░░░██║░░░██████╦╝
                            ╚═════╝░░░░╚═╝░░░╚═════╝░                            
 ''')
logo()
time.sleep(2)
print("Welcome To The Super Telephone Book\n What do you want to do next?")


def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')


def main():
	with open("names.txt","a") as fo:
		# Input the user data
		data = input("Whats your name and telephone?: ")
		# write data to the file
		fo.write(os.linesep)
		fo.write(data)

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
	
menu()	
while True:
	answer = int(input("Enter your option:"))
	if answer == 1:
		clear()
		logo()
		main()			
	elif answer == 2:
		clear()
		logo()
		find_contact()
	elif answer == 3:
			clear()
			logo()
			if_four()
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
