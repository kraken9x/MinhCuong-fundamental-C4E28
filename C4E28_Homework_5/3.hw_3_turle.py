from turtle import *


def draw_square(col, len):    
    for i in range(4):
        color(col)
        forward(len)
        left(90)

draw_square("red", 100)

mainloop()