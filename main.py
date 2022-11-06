import turtle as t

tim = t.Turtle()
def triangle():
    tim.left(60)
    tim.forward(100)
    tim.left(120)
    tim.forward(100)
    tim.left(120)
    tim.forward(100)
    tim.left(120)
    tim.forward(100)
    tim.right(60)



def square():
    for i in range(4):
        tim.right(90)
        tim.forward(100)


def pentagon():
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)
    tim.right(72)
    tim.forward(100)


def hexagon():
    for i in range(6):
        tim.right(60)
        tim.forward(100)



def heptagon():
    for i in range(7):
        tim.right(51.42)
        tim.forward(100)


def octagon():
    for i in range(8):
        tim.right(45)
        tim.forward(100)




def nanogon():
    for i in range(9):
        tim.right(40)
        tim.forward(100)



def decagon():
    for i in range(10):
        tim.right(36)
        tim.forward(100)


triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nanogon()
decagon()


