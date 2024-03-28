#Creates a cool spirograph in Python with Turtle

from turtle import Screen, Turtle, color, colormode
import turtle
import random

tim = Turtle()
tim.speed(0)
#Need colormode for RGB
colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255) 
    random_color = (r,g,b)
    return random_color

for x in range(0,36):
    tim.circle(50)
    tim.right(10)
    tim.color(random_color())


screen = Screen()
screen.exitonclick()