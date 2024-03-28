from tkinter import *

def miles_to_km():
    miles = float(input.get())
    km = miles*1.689
    calc.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

my_label = Label(text="is equal to", font=("Arial",12)) 
my_label.place(x=40,y=50)

my_label_2 = Label(text="Miles", font=("Arial",12)) 
my_label_2.place(x=190,y=30)

my_label_3 = Label(text="Km", font=("Arial",12)) 
my_label_3.place(x=190,y=55)

calc = Label(text=miles_to_km,)
calc.place(x=120,y=50)

input = Entry(width=7)
input.insert(END, string="0")
input.place(x=120,y=30)

button = Button(text = "Calculate", command=miles_to_km)
button.place(x=120,y=80)





