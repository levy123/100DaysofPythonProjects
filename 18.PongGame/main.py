from turtle import Screen
from paddle import Paddle
from ball import Ball

paddle_1 = Paddle(x_cor=-350, y_cor=0)
paddle_2 = Paddle(x_cor=350, y_cor=0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

ball = Ball()

game_is_on = True

while game_is_on:
    ball.move()

screen.listen()   
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")
screen.exitonclick()
