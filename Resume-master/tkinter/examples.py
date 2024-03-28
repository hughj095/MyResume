from tkinter import *

window = Tk()
window.title("first GUI")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_label = Label(text="I am a label", font=("Arial",24,"bold")) 
my_label.grid(column=0,row=0)
my_label["text"]
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

input = Entry(width=10)
input.insert(END, string="default value")
input.grid(column=3,row=2)
print(input.get())

button = Button(text = "Click Me", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text = "Click Me 2", command=button_clicked)
button.grid(column=2,row=0)

text = Text(height=5, width=30)
text.focus()
text.insert(END,"Example")
text.grid(column=4,row=2)

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox()
spinbox.place(x=200,y=100)

window.mainloop()