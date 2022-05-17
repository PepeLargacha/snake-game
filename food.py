import random
from turtle import Turtle
FOOD_POSITIONS = [-260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40,
                  -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]


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
        random_pos = tuple(random.choices(FOOD_POSITIONS, k=2))
        if random_pos in [part.pos() for part in snake]:
            return self.refresh(snake)
        else:
            self.goto(random_pos)