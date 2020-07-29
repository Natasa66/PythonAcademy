import turtle
import time
import random

# ideme korytnackou nakreslit stvorec
from typing import Tuple


def stvorec(korytnacka):
    for i in range(4):
        korytnacka.forward(200)
        korytnacka.left(90)


# domcek jednym tahom
def domcek(korytnacka):
    korytnacka.pendown()  # pre istotu pero dole
    korytnacka.forward(300)
    korytnacka.left(135)
    korytnacka.forward(424)
    korytnacka.right(135)
    korytnacka.forward(300)
    korytnacka.left(135)
    korytnacka.forward(213)
    korytnacka.left(90)
    korytnacka.forward(213)
    korytnacka.left(45)
    korytnacka.forward(300)
    korytnacka.left(135)
    korytnacka.forward(424)
    korytnacka.right(135)
    korytnacka.forward(300)


# je tam vela roznych funkcii napr.
# korytnacka.setheading(90)   #otoci len hlavu o 90 stupnov
# penup() a pendown() sluzia na zdvih a polozenie pera - vynechavam useky kreslenia
# pencolor("RED")  - to je jasne - 8 zakladnych farieb, mozu byt aj male pismena - red
# korytnacka2 = turtle.Turtle()
# korytnacka2.pencolor("green")
# korytnacka2.penup()
# korytnacka2.setposition((100,-200))
# korytnacka2.pendown()
# stvorec(korytnacka2)


korytnacka1 = turtle.Turtle()

# stvorec(korytnacka1)

# zistim velkost okna
my_window = korytnacka1.getscreen()
w_height = my_window.window_height()
w_width = my_window.window_width()
house_height = 451
house_width = 400
print(f"height: {w_height}")
print((f"width: {w_width}"))
if w_height > 452 :
    my_yrange = w_height/2
    zmesti_sa=True
else:
    my_yrange = house_height/2
    zmesti_sa = False
    print("domcek sa nezmesti ale nakreslime co sa da")
if w_width > 452:
    my_xrange = w_width / 2
    zmesti_sa = True
else:
    my_xrange = house_height/2
    zmesti_sa = False
    print("domcek sa nezmesti ale nakreslime co sa da")

# nahodne umiestneny domcek
# definujem farby
# vytvorim list
farby = ["RED", "GREEN", "BLUE", "BLACK", "PINK", "PURPLE", "YELLOW"]
for i in range(4):
    # pozicia pre zaciatok kreslenia
    pos_x = random.randint(-my_xrange, my_xrange)
    pos_y = random.randint(-my_yrange, my_yrange)
    korytnacka1.penup()
    uhol = korytnacka1.heading()
    print(f"uhol {i} je {uhol}")
    #korekcia pozicie

    korytnacka1.setposition(pos_x, pos_y)

    # nahodna farba pera
    korytnacka1.pencolor(random.choice(farby))
    # nahodna hrubka pera
    korytnacka1.pensize(random.randint(1, 4))
    korytnacka1.pendown()
    domcek(korytnacka1)

time.sleep(8)
