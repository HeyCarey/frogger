from turtle import Turtle, forward
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

"""Create cars that are 20px high by 40px wide that are randomly 
generated along the y-axis and move to the left edge of the screen. 
No cars should be generated in the top and bottom 50px of the screen 
(think of it as a safe zone for our little turtle). 
Hint: generate a new car only every 6th time the game loop runs. """

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,8)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-200, 200)
            new_car.setposition(270, random_y)
            self.all_cars.append(new_car)

    def moving_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT





