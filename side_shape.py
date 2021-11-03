from turtle import Turtle
class Shape(Turtle):
    SET_POSITIONS = [(-350, 0), (350,0)]
    def __init__(self):
        self.sides = []
        self.create_side_shape()
    def create_side_shape(self):
        for i in self.SET_POSITIONS:
            side_shape = Turtle("square")
            side_shape.color("white")
            side_shape.turtlesize(5, 1)
            side_shape.penup()
            side_shape.goto(i)
            self.sides.append(side_shape)


    #below are the functions that move the left paddle up or down
    def move_left_down(self):
        new_y = self.sides[0].ycor() - 20
        self.sides[0].goto(self.sides[0].xcor(), new_y)


    def move_left_up(self):
        new_y = self.sides[0].ycor() + 20
        self.sides[0].goto(self.sides[0].xcor(), new_y)
    #functions to move the right paddle either up or down
    def move_right_down(self):
        new_y = self.sides[1].ycor() - 20
        self.sides[1].goto(self.sides[1].xcor(), new_y)

    def move_right_up(self):
        new_y = self.sides[1].ycor() + 20
        self.sides[1].goto(self.sides[1].xcor(), new_y)

