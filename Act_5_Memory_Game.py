
from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
"""Tap counter."""
tap_count = 0 

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    """Increasing the tap counter."""
    global tap_count
    tap_count += 1 

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    """Verification in order to know if all the tokens have been uncovered."""
    if all(not hidden for hidden in hide):
        print(f"¡Juego terminado en {tap_count} taps!")

def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        x, y = xy(count)
        if hide[count]:
            square(x, y)
        else:
            up()
            """Centering the number."""
            goto(x + 25, y)  
            color('black')
            write(tiles[count], align='center', font=('Arial', 30, 'normal'))
    
    """Showing the tap counter in the left superior corner."""
    up()
    goto(-180, 180)
    color('black')
    write(f'Taps: {tap_count}', font=('Arial', 20, 'normal'))
    
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        """Centering the number."""
        goto(x + 25, y)
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))
    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()