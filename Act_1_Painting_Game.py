"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector

import math


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

"""Function for draw a circle added"""
def draw_circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    
    radius = math.sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2) / 2
    goto(start.x + radius, start.y) 

    circle(radius)  

    end_fill()

"""Function for draw a rectangle added"""
def rectangle(start, end):
    """Draw rectangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

"""Function for draw a triangle added"""
def triangle(start, end):
    """Draw triangle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
"""SETTING THE ONKEY LISTENERS FUNCTIONS AND ANONYMOUS FUNCTIONS"""
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
"""=============================New Color Added============================="""
onkey(lambda: color('purple'), 'P')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
"""=============================Function for draw a circle added============================="""
onkey(lambda: store('shape', draw_circle), 'c')
"""=============================Function for draw a rectangle added============================="""
onkey(lambda: store('shape', rectangle), 'r')
"""=============================Function for draw a triangle added============================="""
onkey(lambda: store('shape', triangle), 't')
done()