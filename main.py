import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

timmy = Player()
score = Scoreboard()
cars = CarManager()

screen.onkey(timmy.go_up, "Up")
screen.onkey(timmy.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.moving_car()

    #detect collision with car
    for car in cars.all_cars:
        if car.distance(timmy) < 20:
            game_is_on = False
            score.start_over()

    #detect a successful crossing
    if timmy.is_at_finish():
        timmy.go_to_start()
        cars.level_up()
        score.scoring()

screen.exitonclick()
