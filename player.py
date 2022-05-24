from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() > -280:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def go_left(self):
        if self.xcor() > -280:
            self.setheading(180)
            self.forward(MOVE_DISTANCE)

    def go_right(self):
        if self.xcor() < 280:
            self.setheading(0)
            self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def jump(self):
        self.forward(280)
