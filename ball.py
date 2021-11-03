from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.sleep_time = 0.1
        self.speed_num = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y =10
    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y *= -1
    def bounce_x(self):
        self.x *= -1
        self.sleep_time *= 0.9
    def reset_position(self):
        self.goto(0,0)
        #go opposite direction to the
        self.bounce_x()
    def increase_speed(self):
        self.speed("fastest")








