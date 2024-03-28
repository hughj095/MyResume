# Flashcard GUI to study French

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import pandas
import time

#VARIABLES
BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"

data = pandas.read_csv("./tkinter/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = []
to_learn = {}

try:
    data = pandas.read_csv(".tkinter/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./tkinter/data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=logo_img)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text = "English", fill=WHITE)
    canvas.itemconfig(card_word, text=current_card["English"], fill=WHITE)
    canvas.itemconfig(card_background, image = back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./tkinter/data/words_to_learn.csv", index=False)
    next_card()

#TKINTER ENVIRONMENT
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

#IMAGES
logo_img = PhotoImage(file="./tkinter/images/card_front.png")
back_img = PhotoImage(file="./tkinter/images/card_back.png")
x_img = PhotoImage(file="./tkinter/images/wrong.png")
check_img = PhotoImage(file="./tkinter/images/right.png")

#INITIAL CANVAS
card_background = canvas.create_image(400,263, image=logo_img)
card_title = canvas.create_text(400,150,text="Title", font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="word", font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0, columnspan=2)

#BUTTONS
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=0)

check_button = Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(row=1,column=1)

next_card()

window.mainloop()