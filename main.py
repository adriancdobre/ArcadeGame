from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Arcade Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()


    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()




screen.exitonclick()
