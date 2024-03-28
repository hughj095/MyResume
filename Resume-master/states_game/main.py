# This program is a game for user input of a state name, 
# then displays the name on its corresponding state in the gif map

import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "./states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./states_game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state name?").title()
    if answer_state == "Exit":
        break
    print(answer_state)
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(state_data.state.item())
        all_states.remove(answer_state)

df = pandas.DataFrame(all_states)
df.to_csv('./states_game/states_to_learn.csv')


turtle.mainloop()
screen.exitonclick()