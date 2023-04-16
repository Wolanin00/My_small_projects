from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.goto(100, 100)
timmy.right(90)
timmy.forward(100)
timmy.color('red')

my_screen = Screen()
my_screen.exitonclick()
