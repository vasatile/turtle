import turtle
from turtle import Turtle, Screen
import  random

jim = Turtle()

turtle.colormode(255)
directions = [0,90, 180, 270]
jim.pensize(15)
jim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



for _ in range(200):
    jim.color(random_color())
    jim.forward(30)
    jim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()