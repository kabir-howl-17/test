import turtle
from turtle import *

bgcolor("black")

speed(0)
hideturtle()
left(90)
forward(50)
for i in range(150):
    color("red")
    circle(i*0.7)
    color("yellow")
    circle(i*0.5)
    right(3)
    forward(3)
color("black")

for i in range(150,0,-1):

    color("red")
    circle(i*0.7)
    color("yellow")
    circle(i*0.5)
    right(3)
    forward(3)


done()