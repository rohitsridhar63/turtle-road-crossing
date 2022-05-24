from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = .5
MOVE_INCREMENT = 1


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.all_cars_backwards = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 50)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            random_start = random.randint(1, 2)
            if random_start == 1:
                new_car.goto(300, random_y)
                self.all_cars.append(new_car)
            else:
                new_car.goto(-300, random_y)
                self.all_cars_backwards.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        for car in self.all_cars_backwards:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
