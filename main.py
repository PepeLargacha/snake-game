from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
from gameconfig import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_SPEED
import time

SPEEDS = {1: 0.5, 2: 0.4, 3: 0.3, 4: 0.2, 5: 0.1}

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
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


def reset_round():
    snake.reset_snake()
    score_board.reset_scoreboard()
    new_round()


screen.onkey(reset_round, 'n')


def new_round():
    score_board.draw_score()
    game_end = False
    while not game_end:
        screen.update()
        time.sleep(SPEEDS[GAME_SPEED])
        snake.move()

        # Detect collision with food.
        if snake.head.distance(food) < 15:
            food.refresh(snake.snake_parts)
            score_board.increment_score()
            snake.extend()

        # Detect collision with wall.
        if snake.head.xcor() > (SCREEN_WIDTH / 2 - 10) or\
                snake.head.xcor() < (SCREEN_WIDTH / 2 -10) * (-1) or\
                snake.head.ycor() > (SCREEN_HEIGHT / 2 - 10) or\
                snake.head.ycor() < (SCREEN_HEIGHT / 2 -10) * (-1):
            game_end = True
            score_board.game_over()

        # Detect collision with tail.
        for part in snake.snake_parts[1:]:
            if snake.head.distance(part) < 10:
                game_end = True
                score_board.game_over()


new_round()
screen.exitonclick()
