import turtle
from turtle import Turtle, Screen
import colorgram
import random
turtle.colormode(255)

# colors = list(colorgram.extract('image.jpg', 22))
#
# colors_list = []
# for color in colors:
#     colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(colors_list)

colors_list = [(235, 239, 246), (247, 239, 242), (135, 164, 199), (223, 151, 105), (31, 44, 63), (200, 137, 148), (160, 61, 51), (235, 212, 93), (49, 100, 139), (138, 181, 162), (147, 64, 72), (56, 49, 47), (161, 32, 30), (62, 115, 100), (228, 165, 171), (51, 40, 43), (169, 29, 33), (210, 86, 76), (236, 167, 156), (34, 60, 54)]
tim = Turtle()
screen = Screen()

posy = -250
posx = -300

tim.hideturtle()
tim.penup()
tim.setx(posx)
tim.sety(posy)
for x in range(10):
    tim.penup()
    tim.setx(posx)
    tim.sety(posy)
    for _ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(colors_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    posy += 50

screen.exitonclick()
