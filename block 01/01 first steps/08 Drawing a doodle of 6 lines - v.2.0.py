# Drawing a doodle of 6 lines

from turtle import *
# Set the variables
num_lines = 6
num_waves = 3
# Move to the initial position and set the starting angle
goto(0,0)
left(15)
# Draw 6 lines
for line in range (1,num_lines + 1):
    # Draw a line composed of 3 waves
    for wave in range (0,num_waves):
        right(30)
        forward(75)
        right(-30)
        forward(75)
    # Move to the starting point of the next line
    penup()
    goto(0,-10 * line)
    pendown()

done()