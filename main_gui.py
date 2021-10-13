import tkinter as tk
from tkinter import ttk
from os import remove, path
from tkinter.messagebox import showinfo
from ttkthemes import ThemedTk
import subprocess 
root = ThemedTk(themebg=True)
root.set_theme('yaru')
root.title("Super Telephone Book") 
screen_width= root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
screen_width = str(screen_width)
screen_height = str(screen_height)
root.geometry('640x640')
wrong_inputs = []
left_c_bracket = "}"
right_c_bracket = "{"
Buttons = []
def notepad_run():
	subprocess.run(["notepad", edit_path])
def back_button_command():
    clear()
    menu()
def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list
def clear():
    widget_list = all_children(root)
    for item in widget_list:
        item.pack_forget()
back_button = ttk.Button(root, text="Cancel",command=back_button_command)
def First_Name():
    global first_name, first_name_input
    first_name = tk.StringVar()
    first_name_input = ttk.Entry(root, textvariable=first_name)
    first_name_label = ttk.Label(root, text="Input your name")
    first_name_label.pack()
    first_name_input.pack()

def Surname():
    global surname
    surname = tk.StringVar()
    surname_input = ttk.Entry(root, textvariable=surname)
    surname_label = ttk.Label(root, text="Input your surname")
    surname_label.pack()
    surname_input.pack()

def Phonenumber():
    global phone_number
    phone_number = tk.StringVar()
    phone_number_input = ttk.Entry(root, textvariable=phone_number)
    phone_number_label = ttk.Label(root, text="What's your telephone number")
    phone_number_label.pack()
    phone_number_input.pack()

def Address():
    global address
    address = tk.StringVar()
    address_input = ttk.Entry(root, textvariable=address)
    adress_label = ttk.Label(root, text="Input your address")
    adress_label.pack()
    address_input.pack()

def Zip_Code():
    global zip_code
    zip_code = tk.StringVar()
    zip_code_input = ttk.Entry(root, textvariable=zip_code)
    zip_code_label = ttk.Label(root, text="Whats your zip code?")
    zip_code_label.pack()
    zip_code_input.pack()

def Email_Address():
    global email_address
    email_address = tk.StringVar()
    email_address_input = ttk.Entry(root, textvariable=email_address)
    email_address_label = ttk.Label(root, text="Input your email address")
    email_address_label.pack()
    email_address_input.pack()
def Birthday():
    global birthday
    birthday = tk.StringVar()
    birthday_input = ttk.Entry(root, textvariable=birthday)
    birthday_label = ttk.Label(root, text="When where you born")
    birthday_label.pack()
    birthday_input.pack()
def Save_Info_Button_Command():
    vars_get()
    if not first_name.get().isalpha():
        wrong_inputs.append("First_Name")
    if not surname.get().isalpha():
        wrong_inputs.append("Surname")
    if zip_code.get().isalpha():
        wrong_inputs.append("Zip Code")
    if len(wrong_inputs) > 0:
        showinfo("Wrong Input", "Values {} are wrong. Try again".format(wrong_inputs))
        wrong_inputs.clear()
    else:
        txt_name = first_name_2 + "_" + surname_2
        data = "First Name: " + first_name_2, "Surname: " +surname_2, "Telephone Number: " + phone_number_2, "Location: " + "2", "Address: " +address_2, "Zip Code: " + zip_code_2, "Email Address: " +email_address_2, "Birthday: " + birthday_2
        data = list(data)
        with open('super-telephone-book\\'+txt_name+'.txt', "w+") as sh:
            for i in data:
                sh.write(i)
                sh.write("\n")
        with open("super-telephone-book\\names.txt", "w+") as main_catalog:
            main_catalog.write("\n")
            main_catalog.write(txt_name)
        clear()
        completed_successfully_label()
        menu()
    
def completed_successfully_label():
    showinfo('Success','Completed Successfully')      

    
def vars_get():
    global first_name_2, surname_2, phone_number_2, address_2, email_address_2, birthday_2,zip_code_2
    first_name_2 = str(first_name.get())
    surname_2 = str(surname.get())
    phone_number_2 = str(phone_number.get())
    address_2 = str(address.get())
    email_address_2 = str(email_address.get())
    birthday_2 = str(birthday.get())
    zip_code_2 = str(zip_code.get())
    first_name_2 = first_name_2.capitalize()
    surname_2 = surname_2.capitalize()
    address_2 = address_2.capitalize()
def Save_Info_Button():
    save_info_button = ttk.Button(
        root,
        text="Submit",
        command=Save_Info_Button_Command
    )
    save_info_button.pack()
def option_one():
    clear()
    First_Name()
    Surname()
    Phonenumber()
    Address()
    Email_Address()
    Zip_Code()
    Birthday()
    Save_Info_Button()
    back_button.pack()

def option_three():
    clear()
    fo = open("super-telephone-book\\names.txt", "r")
    contact_list = fo.readlines()
    for i, contact in enumerate(contact_list):
        # remove \n
        contact = contact.strip("\n")
        # create buttons and pass index to callback/command
        button = ttk.Button(root, text=contact, command=lambda index=i: option_three_command(index))
        button.pack()
        # update list of created buttons
        Buttons.append(button)
    back_button.pack()
def option_three_command(i):
    # Get text of clicked (=indexed) button
    delete_input = str(Buttons[i].cget("text"))
    delete_path = 'super-telephone-book\\'+delete_input+'.txt'
    if path.exists(delete_path):
        remove(delete_path)
        Buttons[i].destroy()
        name_delete = open("super-telephone-book\\names.txt", "w+")    
        name_delete_2 = name_delete.readlines()
        for line in name_delete_2:
            if line.strip("\n") != delete_input:
                name_delete_2.write(line)

    else:
        showinfo('Error', 'This file does not exist')
    print(f"Delete name '{delete_input}'")
def edit_contact():
    clear()
    fl = open("super-telephone-book\\names.txt", "r")
    contact_list = fl.readlines()
    for i, contact in enumerate(contact_list):
        # remove \n
        contact = contact.strip("\n")
        # create buttons and pass index to callback/command
        button = ttk.Button(root, text=contact, command=lambda index=i: edit_contact_command(index))
        button.pack()
        # update list of created buttons
        Buttons.append(button)
    back_button.pack()
def edit_contact_command(i):
    global edit_path
    # Get text of clicked (=indexed) button
    edit_input = str(Buttons[i].cget("text"))
    edit_path = 'super-telephone-book\\'+edit_input+'.txt'
    if path.exists(edit_path):
        notepad_run()
    else:
        showinfo("Please input a valid contact")
        
def contact_list_on_screen():
    with open("super-telephone-book\\names.txt", "r") as clos:
        clear()
        all_contacts = clos.readlines()
        for item in all_contacts:
            ttk.Label(root,text=item).pack()
        back_button.pack()

def menu():
    option_one_button = ttk.Button(
        root,
        text="Add A Contact",
        command=option_one
    )
    option_three_button = ttk.Button(
        root,
        text='Delete Contact',
        command=option_three

    )
    option_four_button = ttk.Button(
        root,
        text="Contact List",
        command=contact_list_on_screen

    )
    option_five_button = ttk.Button(
        root,
        text="Edit A Contact",
        command=edit_contact

    )
    def buttons_pack():
        option_one_button.pack()
        option_three_button.pack()
        option_four_button.pack()
        option_five_button.pack()
    buttons_pack()


menu()
root.mainloop() # always run