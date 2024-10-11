from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list1 = [random.choice(letters) for char in range(nr_letters)]
password_list2 = [random.choice(symbols) for char in range(nr_symbols)]
password_list3 = [random.choice(numbers) for char in range(nr_numbers)]
password_list = password_list1 + password_list2 + password_list3

random.shuffle(password_list)

password = ''.join(password_list)

def generate_pwd():
    global password
    enter_pwd.delete(0, END)
    enter_pwd.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def prn():

    if len(enter_mail.get()) == 0 or len(enter_pwd.get()) == 0:
        messagebox.showerror('Error', "Website/Password can not remain empty")
    else:
        response = messagebox.askyesno('Confirm', 'Are you sure you want to save this password?')
        if response == True:
            with open('data.txt', mode= 'a') as file:
                file.write(f"{enter_web.get()} | {enter_mail.get()} | {enter_pwd.get()}\n")
            enter_web.delete(0, END)
            enter_pwd.delete(0, END)
        else:
            pass

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady =50)

canvas = Canvas(width = 200, height = 200)
pic = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image = pic)
canvas.grid(column = 1, row = 0)

web_text = Label(text = 'Website:')
web_text.grid(column = 0, row = 1)

enter_web = Entry(width = 35)
enter_web.grid(column = 1, row = 1, columnspan = 2)
enter_web.focus()

mail_text = Label(text = 'Email/Username:')
mail_text.grid(column = 0, row = 2)

enter_mail = Entry(width = 35)
enter_mail.grid(column = 1, row = 2, columnspan = 2)
enter_mail.insert(0, 'karanwadhwani2005@gmail.com')

generate_button = Button(text = 'Generate Password:', command= generate_pwd)
generate_button.grid(column = 2, row = 3)

pwd_text = Label(text = 'Password:')
pwd_text.grid(column = 0, row = 3)

enter_pwd = Entry(width = 21)
enter_pwd.grid(column = 1, row = 3)

add_button = Button(text = 'Add', width = 30, command=prn)
add_button.grid(column = 1, row = 4, columnspan = 2)


window.mainloop()