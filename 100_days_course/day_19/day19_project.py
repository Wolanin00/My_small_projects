import time
import random
from turtle import Turtle, Screen
import keyboard


def random_color():
    screen.colormode(255)
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


def right_press():
    my_turtle.right(10)


def left_press():
    my_turtle.left(10)


def go_forward():
    my_turtle.forward(10)


def go_backward():
    my_turtle.backward(10)


def change_turtle_color():
    my_turtle.color(random_color())


def close_screen():
    global is_screen_on
    is_screen_on = False


my_turtle = Turtle()
screen = Screen()
my_turtle.shape('turtle')


is_screen_on = True
is_pen_down = True
while is_screen_on:
    if keyboard.is_pressed('esc'):
        close_screen()
    elif keyboard.is_pressed('right') and keyboard.is_pressed('up'):
        right_press()
        go_forward()
    elif keyboard.is_pressed('left') and keyboard.is_pressed('up'):
        left_press()
        go_forward()
    elif keyboard.is_pressed('right') and keyboard.is_pressed('down'):
        right_press()
        go_backward()
    elif keyboard.is_pressed('left') and keyboard.is_pressed('down'):
        left_press()
        go_backward()
    elif keyboard.is_pressed('up'):
        go_forward()
        time.sleep(0.02)
    elif keyboard.is_pressed('down'):
        go_backward()
        time.sleep(0.02)
    elif keyboard.is_pressed('right'):
        right_press()
        time.sleep(0.02)
    elif keyboard.is_pressed('left'):
        left_press()
        time.sleep(0.02)
    elif keyboard.is_pressed(','):
        my_turtle.penup()
        is_pen_down = False
    elif keyboard.is_pressed('.'):
        my_turtle.pendown()
        is_pen_down = True
    elif keyboard.is_pressed('r'):
        change_turtle_color()
        time.sleep(0.01)
    elif keyboard.is_pressed('c'):
        my_turtle.clear()
        if is_pen_down:
            my_turtle.penup()
        my_turtle.home()
        if is_pen_down:
            my_turtle.pendown()
