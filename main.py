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
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh(snake.snake_parts)
        score_board.increment_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_end = True

    # Detect collision with tail.
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_end = True
            score_board.game_over()

score_board.game_over()
screen.exitonclick()
