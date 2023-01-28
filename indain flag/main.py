# Made with Chat api AI and Debugged by me- Rishu [Yt- @rishusnehansh || ig- @igx Cahuhang]

#import turtle
import turtle
from turtle import *

# screen for output
screen = turtle.Screen()
# Defining a turtle Instance
flag = turtle.Turtle()
speed(1)

# initially penup()
flag.penup()
flag.goto(-200, 125)
flag.pendown()

# Draw the saffron & white stripe
flag.color("#FF9933")
flag.begin_fill()
flag.forward(400)
flag.right(90)
flag.forward(84)
flag.right(90)
flag.forward(400)
flag.end_fill()
flag.left(90)
flag.forward(84)

# Draw the green stripe
flag.color("green")
flag.begin_fill()
flag.forward(84)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(84)
flag.end_fill()

# Draw the circle
flag.color("white")
flag.goto(35, 0)
flag.pendown()
flag.color("navy")
flag.begin_fill()
flag.circle(35)
flag.end_fill()
flag.penup()
flag.goto(30, 0)
flag.pendown()
flag.color("white")
flag.begin_fill()
flag.circle(30)
flag.end_fill()

#Mini Blue Circles of Flag
flag.penup()
flag.goto(-27, -4)
flag.pendown()
flag.color("navy")
for i in range(24):
    flag.begin_fill()
    flag.circle(2)
    flag.end_fill()
    flag.penup()
    flag.forward(7)
    flag.right(15)
    flag.pendown()

# Small Blue Circle
flag.color("navy")
flag.penup()
flag.goto(10, 0)
flag.pendown()
flag.begin_fill()
flag.circle(10)
flag.end_fill()

#The spokes of India Flag
flag.penup()
flag.goto(0, 0)
flag.pendown()
flag.pensize(1)
for i in range(24):
    flag.forward(30)
    flag.backward(30)
    flag.left(15)

#for stick of the flag
flag.color("black")
flag.pensize(1)
flag.penup()
flag.goto(-200,125)
flag.right(180)
flag.pendown()
flag.forward(252)
# flag.forward(84)
flag.left(90)
flag.forward(400)
flag.left(90)
flag.forward(252)
flag.left(90)
flag.forward(400)

# Hide the turtle
flag.hideturtle()

# Keep the screen open
turtle.done()
