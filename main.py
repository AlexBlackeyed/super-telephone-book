import os
import time
import colorama
from colorama import Fore
from colorama import Style
from subprocess import call


def main():
	# opens file in write mode
	fo = open("names.txt","a")
	# Input the user data
	data = input("Whats ur name and telephone?: ")
	# write data to the file
	fo.write(os.linesep)
	fo.write(data)
	# close the file
	fo.close()

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
	with open("names.txt", "r") as f:
						
						# read data line by line 
						dataa = f.readlines()
					# open file in write mode
	with open("names.txt", "w") as f:
		for line in dataa :							
		# condition for data to be deleted
			if line.strip("\n") != delete_input : 
								f.write(line)				
					
				


def if_four():
	# opens txt file in read mode
	fo = open("names.txt", 'r')
	#reads the txt
	ContactList=fo.read()
	#prints everything that is written in the txt file
	print(ContactList)
	print('\n')




print("                              SUPER TELEPHONE BOOK")
time.sleep(2)
#just a cool looking ascii 
print('''   
                            ░██████╗████████╗██████╗░
                            ██╔════╝╚══██╔══╝██╔══██╗
                            ╚█████╗░░░░██║░░░██████╦╝
                            ░╚═══██╗░░░██║░░░██╔══██╗
                            ██████╔╝░░░██║░░░██████╦╝
                            ╚═════╝░░░░╚═╝░░░╚═════╝░                            
 ''')

time.sleep(2)
print("Welcome To The Super Telephone Book\n What do you want to do next?")



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
		main()			
	elif answer == 2:
			find_contact()
	elif answer == 3:
			if_four()
			delete_input = input("Input the contact from the ones above that you want to be deleted!\n Note. Copy and paste exactly the contact otherwise it wont work :D\n >")
			delete_contact()	
	elif answer == 4:			
			if_four()	
	else:
		print("Input a number given in the options")
		menu()
	if answer == 99:
		print("Thanks for using this program")
		quit()		
