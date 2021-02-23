from turtle import Turtle, Screen

class Box(Turtle):
    def wall(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("brown")
        self.goto(-290, 290)
        self.pendown()
        self.pensize(10)
        self.goto(290, 290)
        self.right(90)
        self.goto(290, -290)
        self.right(90)
        self.goto(-290, -290)
        self.right(90)
        self.goto(-290, 290)

    def box(self):
        self.penup()
        self.goto(-40, 40)
        self.pendown()
        self.hideturtle()
        self.forward(200)
        # self.forward(6000)
