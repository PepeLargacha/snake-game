from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(-20, 270)
        self.draw_score()

    def increment_score(self):
        self.clear()
        self.score += 10
        self.draw_score()

    def draw_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
