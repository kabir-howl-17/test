import turtle
import math
from turtle import *

aainu = turtle.Turtle()

aainu.color("purple", "blue")
aainu.begin_fill()
for i in range(4):
        aainu.forward(200)
        aainu.left(90)

aainu.end_fill()
aainu.penup()
aainu.backward(250)
aainu.pendown()
aainu.color("purple", "blue")
aainu.begin_fill()
for i in range(4):
        aainu.forward(200)
        aainu.left(90)

aainu.end_fill()