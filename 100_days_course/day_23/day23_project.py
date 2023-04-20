import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title("Turtle crossing road")
screen.tracer(0)

turtle_tim = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle_tim.go_forward, "Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    car_manager.move()

    # Generate random cars
    random_chance = random.randint(1, 6)
    if random_chance == 1:
        car_manager.add_new_car()

    # Defect collision turtle with car
    for car in car_manager.cars:
        if car.distance(turtle_tim) < 24:
            scoreboard.game_over()
            is_game_on = False

    # Detect if turtle hit top edge
    if turtle_tim.ycor() > 280:
        scoreboard.next_level()
        car_manager.increment_speed()
        turtle_tim.go_to_start()

screen.exitonclick()
