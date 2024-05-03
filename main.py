from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.listen()
screen.tracer(0)

r_paddle = Paddle(x_cordinate=350, y_cordinate=0)
screen.onkey(key= "Up", fun= r_paddle.go_up)
screen.onkey(key= "Down", fun= r_paddle.go_down)

l_paddle = Paddle(x_cordinate=-350, y_cordinate=0)
screen.onkey(key= "w", fun= l_paddle.go_up)
screen.onkey(key= "s", fun= l_paddle.go_down)

ball = Ball()
scoreboard = Scoreboard()
sleep_time = 0.1

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()
    if ball.distance(x=ball.xcor(), y=300) < 15 or ball.distance(x=ball.xcor(), y=-300) < 15:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        if sleep_time > 0:
            sleep_time -= 0.018

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        sleep_time = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        sleep_time = 0.1

screen.exitonclick()