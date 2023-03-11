from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["cornflower blue", "turquoise", "medium sea green", "green yellow", "yellow", "dark orange", "red", "deep pink", "orchid", "medium violet red"]
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()