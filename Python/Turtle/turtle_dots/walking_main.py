from turtle import Screen, Turtle, color
import turtle
import random

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)


direction = [0,90,180,270]

sides = 3
length = 50
steps = 50

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255) 
    random_color = (r,g,b)
    return random_color
#def ran
tim.speed(0)
for x in range(steps):
    tim.color(random_color())
    width = random.randrange(1,20)
    tim.width(width)
    tim.forward(20)
    num = random.choice(direction)
    tim.right(num)



screen = Screen()
screen.exitonclick()




