from turtle import Turtle
from gameconfig import SCREEN_HEIGHT, ALIGNMENT, FONT


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.pencolor("red")
        self.hideturtle()
        self.penup()
        self.get_highscore()

    def increment_score(self):
        self.score += 10
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.goto(0, SCREEN_HEIGHT / 2 - 20)
        self.write(f'Score: {self.score}     High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("log.txt", mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.draw_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -30)
        self.write("Press 'N' to play again.", align=ALIGNMENT, font=FONT)

    def get_highscore(self):
        try:
            with open("log.txt") as file:
                high_score = int(file.read())
                self.high_score = high_score
        except:
            self.high_score = 0
