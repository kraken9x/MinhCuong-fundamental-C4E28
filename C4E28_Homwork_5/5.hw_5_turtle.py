from turtle import *


def draw_star(x, y, len):
    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        color("black")
        forward(len)
        right(144)

draw_star(-100, 100, 200)
mainloop()