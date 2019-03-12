from turtle import *


def draw_star(x, y, len):
    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        color("black")
        forward(len)
        right(144)


speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)


mainloop()