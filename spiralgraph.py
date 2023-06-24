import turtle
from turtle import Turtle, Screen
import  random

jim = Turtle()


turtle.colormode(255)
directions = [0,90, 180, 270]
jim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
def draw_spiralgraph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)
        jim.circle(100)

draw_spiralgraph(random.randint(3, 6))











screen = Screen()
screen.exitonclick()
