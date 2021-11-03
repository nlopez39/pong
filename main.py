from turtle import Screen
from side_shape import Shape
from ball import Ball
from scoreboard import Score
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("pong")
screen.tracer(0)


#creates left and right paddles

paddle = Shape()
#creates ball
ball = Ball()
# create score board
scoreboard = Score()

#these functions move our paddles up and down respectively
screen.listen()
screen.onkey(paddle.move_left_down, "Down")
screen.onkey(paddle.move_left_up, "Up")
screen.onkey(paddle.move_right_down, "w")
screen.onkey(paddle.move_right_up, "s")


#must place the upgrade function in a while loop if you want everything to worl
game_on = True
while game_on:
    time.sleep(ball.sleep_time)
    screen.update()
    ball.move_ball()
    # make bounce | bounce when we hit the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detect paddle
    #detect right paddle
    if ball.distance(paddle.sides[1]) < 60 and ball.xcor() > 340:
        ball.bounce_x()

#detect left paddle
    if ball.distance(paddle.sides[0]) < 60 and ball.xcor() < -340:
        ball.bounce_x()
    #if right paddle shoots
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_right()

    #if left paddle shoots
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_left()






























screen.exitonclick()