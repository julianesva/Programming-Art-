from random import *
from turtle import *
from freegames import path

"""IMPORTANT: In order to make a better game or a game that improve the intelligence or memory of the players i implemented letters instead of numbers in this version of the game."""

"""Initialize the car variable with the image path"""
car = path('car.gif') 

"""List of 32 letters for the game"""
letters = [chr(ord('A') + i) for i in range(32)] 
"""Create pairs of letters for a total of 64 tiles"""
tiles = list(letters) * 2  
state = {'mark': None}
hide = [True] * 64
"""Tap counter."""
tap_count = 0  


def square(x, y):
    """Draws a white square with a black border at (x, y)."""
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
    """Converts coordinates (x, y) to a tile index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Converts the tile index to coordinates (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Updates the mark and hidden tiles based on the tap."""
    global tap_count  
    """Increasing the tap counter."""
    tap_count += 1  

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    """Verification in order to know if all the tokens have been uncovered."""
    if all(not hidden for hidden in hide):
        print(f"Game over in {tap_count} taps!")


def draw():
    """Draws the image and the tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Draw the tiles
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

    """Display the letter on the temporarily selected tile"""
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        """Centering the number."""
        goto(x + 25, y)  
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)  # Shuffle the tiles
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
