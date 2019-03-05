from turtle import *

temp = 3
for c in ['red', 'blue', 'brown', 'yellow', 'grey']:
    color(c)
    for i in range(temp):
        forward(100)
        left(360/temp)
    temp += 1

mainloop()