from turtle import Turtle
STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]


    def create_snake(self):
        for pos in STARTING_POSITIONS:
            t = Turtle('square')
            t.penup()
            t.color('white')
            t.goto(pos)
            self.snake_parts.append((t))


    def move(self):
        snake_body_position = list(map(Turtle.pos, self.snake_parts[::-1]))
        for i, turtle in enumerate(self.snake_parts[::-1]):
            if i == len(self.snake_parts) - 1:
                turtle.fd(MOVE_DISTANCE)
            else:
                new_pos = snake_body_position[i+1]
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

