from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake by Pepe")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_end = False
while not game_end:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increment_score()


screen.exitonclick()
