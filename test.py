# Using The Turtle Library
import turtle
from turtle import *
t = Turtle()

#  Our First Line and Shapes
t.shape('turtle')
""" t.forward(200) """


def message(input):
    print(input)
message("Hello Class")
message("Hola Class")
message("Good Afternoon")

# Shapes in Turtle
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


""" def rectangle(x,y):
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
triangle(90) """

# Starting "Loops in Python"
""" for i in range(3):
    print(i) """

# Refactor and Challenges
""" def square():
    for i in range(4):
      t.forward(100)
      t.left(90)


t.speed(20)


def circle():
   for i in range(61):
    square()
    t.right(5)
circle() """

# Variables
""" sidelength = 100
rotate = 120
def triangle(x,y):
   for i in range(3):
      t.forward(x)
      t.left(y)
triangle(100,120) """

# Manipulating Variables
""" def square(x,y):
   for i in range(4):
      t.forward(x)
      t.left(y)


def doubleSquares(iRange):
   length = 25
   for i in range(iRange):
      square(length,90)
      length = length * 2
doubleSquares(5) """

# Assesment
""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)


def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length,90)
        length = length + 5
        t.right(5)
doubleSquares(61) """

# Assesment 2
t.speed(200)

def star(x,y):
    for i in range(5):
       t.forward(x)
       t.left(144)


def doubleStars(iRange):
    length = 5
    for i in range(iRange):
        star(length,144)
        t.right(5)
        length = length + 5
doubleStars(65)


turtle.done()