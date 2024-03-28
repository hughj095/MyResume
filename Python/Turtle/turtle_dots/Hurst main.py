from turtle import Screen, Turtle, color, colormode
import turtle
import random
import colorgram

#Hurst Painting example in python with Turtle

# grabbed RGB colors from jpg example from web
colors = colorgram.extract('dots.jpg',9)
print(colors)
tim = Turtle()
tim.speed(0)
#Need colormode for RGB
colormode(255)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

#print(rgb_colors)

#built color list from jpg
color_list = [(226, 231, 236), (58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171), (224, 234, 230), (141, 178, 204)]

#drawing similar painting in python
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(250)
tim.setheading(0)

for y in range(1,6):
    tim.penup
    for x in range(1,11):
        tim.color = random.choice(color_list)
        c = tim.color
        tim.dot(10,c)
        tim.penup()
        tim.forward(20)
    tim.left(90)
    tim.forward(20)
    tim.left(90)
    tim.forward(20)
    for y in range (1,11):
        tim.color = random.choice(color_list)
        c = tim.color
        tim.dot(10,c)
        tim.penup()
        tim.forward(20)
    tim.right(90)
    tim.forward(20)
    tim.right(90)
    tim.forward(20)


screen = Screen()
screen.exitonclick()