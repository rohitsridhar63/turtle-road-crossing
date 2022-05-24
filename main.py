import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(player.go_up, 'w')
screen.onkey(player.go_down, 's')
screen.onkey(player.go_left, 'a')
screen.onkey(player.go_right, 'd')
screen.onkey(player.jump, 'y')

game_is_on = True
while game_is_on:

    time.sleep(0.01)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with all cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    for car in car_manager.all_cars_backwards:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
