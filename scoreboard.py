from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.increase_level()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER!', align='center', font=FONT)
