# Draw squares accross page

from turtle import *

number_of_shapes = 4

for shape in range(1,number_of_shapes + 1):
    # Draw a square
    for sides in range(1,5):
        forward(40)
        right(90)

    # Move forward to start position of next square
    penup()
    forward(50)
    pendown()
