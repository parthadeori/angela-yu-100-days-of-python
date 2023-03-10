from turtle import Turtle, Screen
import random

tim = Turtle()

colors = ["cornflower blue", "turquoise", "medium sea green", "green yellow", "yellow", "dark orange", "red", "deep pink", "orchid", "medium violet red"]

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)



screen = Screen()
screen.exitonclick()