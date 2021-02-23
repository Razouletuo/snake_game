from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score_board import Score_Board
from UI import Box
import time


turtle = Turtle()
screen = Screen()
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score_Board()
walls = Box()

screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("my_snake_Game")
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
walls.wall()
is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.point()
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        turtle.color("red")
        is_on = False
        scoreboard.game_over()

    #detect collison with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_on = False
            scoreboard.game_over()



screen.exitonclick()
