#Fully functional Password generator, with search, 
# and storage GUI into JSON file with exceptions

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

#VARIABLES
WHITE = "#FFFFFF"
TOTALCHAR = 12
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 's', 'y', 'z']
numbers = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@','#','%','^','&','*','(',')']

#FUNCTIONS
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pword_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
                }
                }

    if website == "" or password == "":
        messagebox.showinfo("Warning", "Please don't leave fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \n {website} \n {email} "
                                                        f"\n {password} \n Is it ok to save?")

        if is_ok:
            try: 
                with open("./tkinter/pword_bank.json", "r") as bank:
                    data = json.load(bank)
                    
            except FileNotFoundError:
                with open("./tkinter/pword_bank.json", "w") as bank:
                    json.dump(data, bank, indent=4)
            else:
                data.update(new_data)
                with open("./tkinter/pword_bank.json", "w") as bank:
                    json.dump(data, bank, indent=4)
            finally:
                website_entry.delete(0,END)
                pword_entry.delete(0,END)

def pword_gen():
    total = TOTALCHAR
    pword = ""
    for i in range(1,total):
        randlet = random.randint(0,25)
        randlet = letters[randlet]
        randnum = random.randint(0,9)
        randnum = numbers[randnum]
        randsym = random.randint(0,8)
        randsym = symbols[randsym]
        randord = random.randint(1,3)
        if randord == 1:
            pword = pword+randlet
        if randord == 2:
            pword = pword+str(randnum)
        if randord == 3:
            pword = pword+randsym
    pword_entry.insert(0,pword)
    pyperclip.copy(pword)

def find_password():
    website = website_entry.get()
    try:
        with open("./tkinter/pword_bank.json", "r") as bank:
            data = json.load(bank)
    except FileNotFoundError:
        messagebox.showinfo("error", "No data found")
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(website, f"{email}\n {password}")


#TKINTER ENVIRONMENT
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200,height=200, bg=WHITE)
logo_img = PhotoImage(file="./tkinter/logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(column=1, row=0)

#LABELS
website_label = Label(text="Website:", font=("Arial",12,"bold")) 
website_label.grid(column=0,row=1)

email_label = Label(text="Email/Username:", font=("Arial",12,"bold")) 
email_label.grid(column=0,row=2)

pword_label = Label(text="Password:", font=("Arial",12,"bold")) 
pword_label.grid(column=0,row=3)

#ENTRIES
website_entry = Entry(width=21)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width = 35)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "john.m.hughes84@outlook.com")
pword_entry = Entry(width=21)
pword_entry.grid(column=1,row=3)

#BUTTONS
gen_button = Button(text = "Generate Password", command=pword_gen)
gen_button.grid(column=2,row=3)

add_button = Button(text="Add", command=save)
add_button.grid(column=1,row=4, columnspan=2)

search_button = Button(text="Search", width=13,command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()