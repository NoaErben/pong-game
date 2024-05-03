from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cordinate, y_cordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        self.setposition(x=self.x_cordinate, y=self.y_cordinate)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def go_down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)





