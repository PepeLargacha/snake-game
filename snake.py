from turtle import Turtle

STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
            self.head = self.snake_parts[0]

    def add_segment(self, position):
        part = Turtle('square')
        part.shapesize(stretch_wid=0.9, stretch_len=0.9)
        part.penup()
        part.color('white')
        part.goto(position)
        self.snake_parts.append(part)

    def extend(self):
        self.add_segment(self.snake_parts[-1].pos())

    def reset_snake(self):
        for part in self.snake_parts:
            part.goto(500, 500)
        self.snake_parts.clear()
        self.create_snake()

    def move(self):
        snake_body_position = list(map(Turtle.pos, self.snake_parts[::-1]))
        for i, turtle in enumerate(self.snake_parts[::-1]):
            if i == len(self.snake_parts) - 1:
                turtle.fd(MOVE_DISTANCE)
            else:
                new_pos = snake_body_position[i + 1]
                turtle.goto(new_pos)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
