import random
from turtle import Turtle, Screen


def random_color():
    screen.colormode(255)
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


how_many_turtle = ''
is_how_many_turtle_correct = False
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('gray')

# HOW MANY TURTLE IN RACE
while not is_how_many_turtle_correct:
    how_many_turtle = screen.textinput('How many turtle', 'How many turtle in race (2-8)?')
    if how_many_turtle in [str(item) for item in range(2, 9)]:
        is_how_many_turtle_correct = True

# CREATE TURTLE OBJECTS
all_turtle = []
for item in range(int(how_many_turtle)):
    exec(f'my_turtle{item}=Turtle()')
    exec(f'my_turtle{item}.shape("turtle")')
    exec(f'my_turtle{item}.penup()')
    exec(f'my_turtle{item}.goto(-200,{25*(int(how_many_turtle)-1)-(50*item)})')
    exec(f'all_turtle.append(my_turtle{item})')

# USER BET
user_bet = ''
is_user_bet_correct = False
while not is_user_bet_correct:
    user_bet = screen.textinput('Make your bet', 'Which turtle will win? Enter the number counting from the top')
    if user_bet in [str(item) for item in range(1, int(how_many_turtle)+1)]:
        is_user_bet_correct = True

# TURTLE RACE
win_turtle = 0
list_of_distance = [number for number in range(0, 11)]
is_race_on = True
while is_race_on:
    for ind, turtle in enumerate(all_turtle):
        if turtle.xcor() > 200:
            is_race_on = False
            win_turtle = ind+1
        turtle.forward(random.choice(list_of_distance))

if user_bet == str(win_turtle):
    screen.textinput('You won!', f'Turtle with number {win_turtle} won')
else:
    screen.textinput('You lose!', f'Turtle with number {win_turtle} won')

screen.exitonclick()
