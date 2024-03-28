from operator import indexOf
from turtle import Screen, Turtle, color
import turtle
import random

#input which color will win race?
screen = Screen()
screen.setup(width=500, height=400)

blue = Turtle(shape="turtle")
blue.color("blue")
blue.penup()
blue.goto(-200,180)

red = Turtle(shape="turtle")
red.color("red")
red.penup()
red.goto(-200,150)

green = Turtle(shape="turtle")
green.color("green")
green.penup()
green.goto(-200,120)

yellow = Turtle(shape="turtle")
yellow.color("yellow")
yellow.penup()
yellow.goto(-200,90)

user_bet = screen.textinput(title="bet", prompt="which turtle will win: ")
list = ["blue","red","green","yellow"]
positions = []
winner = ''
def go():
    winner = ''
    jump = random.randrange(1,10)
    select = random.choice(list)

    blue.forward(10)
    if select == "blue":
        blue.forward(jump)

    red.forward(10)
    if select == "red":
        red.forward(jump)

    green.forward(10)
    if select == "green":
        green.forward(jump)

    yellow.forward(10)
    if select == "yellow":
        yellow.forward(jump)

    positions = [blue.xcor(),red.xcor(),green.xcor(),yellow.xcor()]
    for position in positions:
        if position > 150:
            done = True
            winner = position
            return winner, done
    return winner
    return done

done = False
while done == False:
    go()

print(f'the winnner is {winner}')

screen.exitonclick()

