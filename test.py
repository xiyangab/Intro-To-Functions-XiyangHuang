import turtle
from turtle import *
t = Turtle()


t.shape('turtle')
""" t.forward(200) """


def message(input):
    print(input)
message("Hello Class")
message("Hola Class")
message("Good Afternoon")


""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)


def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right() """


def rectangle(x,y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
rectangle(100,125)


def triangle(x):
    t.right(90)
    t.forward(x)
    t.right(120)
    t.forward(x)
    t.right(120)
    t.forward(x)
triangle(90)

