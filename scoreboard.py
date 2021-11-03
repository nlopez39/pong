from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-100,200) #position of the scoreboard
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Courier", 80, "normal"))

    def increase_score_left(self):
        self.l_score +=1
        self.clear()
        self.update_scoreboard() #makes updateing the board easier
    def increase_score_right(self):
        self.r_score +=1
        self.clear()
        self.update_scoreboard()