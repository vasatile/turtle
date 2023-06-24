import turtle
from turtle import Turtle, Screen
import  random

jim = Turtle()




turtle.colormode(255)
directions = [0,90, 180, 270]
# jim.pensize(15)
jim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color




def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        jim.forward(100)
        jim.right(angle)

for shape_side_n in range(3, 10):
    jim.color(random_color())
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()