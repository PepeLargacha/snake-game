import random
from turtle import Turtle
from gameconfig import SCREEN_WIDTH, SCREEN_HEIGHT

range_x = (int((SCREEN_WIDTH - 40)/2 * -1), int((SCREEN_WIDTH - 40)/2))
range_y = (int((SCREEN_HEIGHT - 40)/2 * -1), int((SCREEN_HEIGHT - 40)/2))

FOOD_X_POSITIONS = list(range(range_x[0], range_x[1], 20))
FOOD_Y_POSITIONS = list(range(range_y[0], range_y[1], 20))

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self, snake=()):
        random_x = random.choice(FOOD_X_POSITIONS)
        random_y = random.choice(FOOD_Y_POSITIONS)
        random_pos = tuple((random_x, random_y))
        if random_pos[0] in [part.xcor for part in snake]\
                and random_pos[1] in [part.ycor for part in snake]:
            return self.refresh(snake)
        else:
            self.goto(random_pos)