from turtle import Turtle, Screen
from UI import Box

ex = Box()

class Score_Board (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update()


    def update(self):
        self.color("red")
        self.write(f"SCORE = {self.score} ", font=("Bookman old style", 20, "normal"), align="center")

    def point(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):

        self.goto(0, 0)
        self.write(f" YOU dead! Game OVER ", font=("Bookman old style", 24, "normal"), align="center")




