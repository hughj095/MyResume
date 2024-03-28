from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open('./snake_game/saved_score.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        with open('./snake_game/saved_score.txt', mode='w') as file:
            file.write(str(self.high_score))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    
    
    #def game_over(self):
        #self.goto(0,0)
        #self.write("GAME OVER", align=ALIGNMENT,font=FONT)
