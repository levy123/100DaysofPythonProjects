from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=None, stretch_len=5, outline=None)
        self.penup()
        self.setpos(x_cor, y_cor)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
