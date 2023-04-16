from turtle import Turtle, Screen
import random
import colorgram


def random_color():
    screen.colormode(255)
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


def draw_square():
    for _ in range(4):
        my_turtle.fd(100)
        my_turtle.right(90)


def dashed_line():
    my_turtle.pencolor('black')
    for _ in range(15):
        my_turtle.pendown()
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)


def draw_multi_shape(how_many_shapes):
    screen.colormode(255)
    for how_many_angles in range(3, how_many_shapes+3):
        my_turtle.pencolor(random_color())
        for _ in range(how_many_angles):
            my_turtle.forward(100)
            my_turtle.right(360/how_many_angles)


def draw_random_walk(road_length: int = 10):
    screen.colormode(255)
    direction = [0, 90, 180, 270]
    my_turtle.pensize(width=6)
    for _ in range(road_length):
        my_turtle.forward(20)
        my_turtle.setheading(random.choice(direction))
        my_turtle.color(random_color())


def draw_spirograph(radius: int = 100, degree_difference: int = 10, draw_random_color: bool = False):
    my_turtle.speed('fastest')
    for _ in range(int(360/degree_difference)):
        if draw_random_color:
            my_turtle.color(random_color())
        my_turtle.circle(radius=radius)
        my_turtle.left(degree_difference)


def extract_color_from_picture(jpg: str, how_many_colors: int = 10):
    rgb_colors = []
    colors = colorgram.extract(jpg, how_many_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgb = (r, g, b)
        rgb_colors.append(rgb)
    return rgb_colors


def draw_hirst_spot_painting(list_of_rgb_colors: list, dots_horizontally: int = 10, dots_vertically: int = 10):
    screen.colormode(255)
    my_turtle.speed('fastest')
    my_turtle.penup()
    my_turtle.hideturtle()

    my_turtle.goto(-((dots_horizontally-1)*25), -((dots_vertically-1)*25))
    for i1 in range(1, dots_vertically+1):
        for i2 in range(1, dots_horizontally+1):
            my_turtle.dot(20, random.choice(list_of_rgb_colors))
            my_turtle.forward(50)
        my_turtle.goto(-((dots_horizontally-1)*25), -((dots_vertically-1)*25)+(i1*50))


# MAIN
screen = Screen()
my_turtle = Turtle()
# my_turtle.shape('turtle')

# SQUARE
# draw_square()

# DASHED_LINE
# dashed_line()

# DRAW_TRIANGLE_SQUARE_PENTAGON_ETC
# draw_multi_shape(3)

# DRAW_RANDOM_WALK
# draw_random_walk(road_length=100)

# MAKE_A_SPIROGRAPH
# draw_spirograph(degree_difference=5, draw_random_color=True)

# HIRST_SPOT_PAINTING
color_list = extract_color_from_picture(jpg='cieple.jpg', how_many_colors=30)
draw_hirst_spot_painting(list_of_rgb_colors=color_list, dots_horizontally=10, dots_vertically=3)


screen.exitonclick()  # do_not_remove
