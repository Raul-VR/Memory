"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from tkinter.ttk import Style
from turtle import *

from freegames import path

import random

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
tapcount = 0
found = 0
n=36

c1=random.randint(2,7)
c2=random.randint(2,7)
while(c2==c1):
    c2=random.randint(2,7)

c3=random.randint(2,7)
while(c3==c1 or c3==c2):
    c2=random.randint(2,7)

def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.random()
      return lista


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
    """RAVR - 24/03/22 - We create a tapcount and found count"""
    global tapcount
    global found
    spot = index(x, y)
    mark = state['mark']
    tapcount += 1

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        found += 1


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #RMEV - 24/03/2022 - We fit the text to the center
        goto(x + 26, y + 4)
        #RMEV - 24/03/2022 - We change the color of the numbers
        color(tiles[mark]*c1, 255-tiles[mark]*c2, 255-tiles[mark]*c3)
        #RMEV - 24/03/2022 - We fit the text to the center
        write(tiles[mark], font=('Arial', 20, 'normal'), align="Center")

    """RAVR - 24/03/22 - a message is created when you win"""
    if found == 32:
        goto(0,100)
        color("white")
        write("¡Ganador!",  align="center", font=("Arial", 30, "bold"))

    goto(0,210)
    write(tapcount, font=('Arial', 25,'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
colormode(255)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
