# Draw a sales graph for a gloves company

from turtle import *

# Set up gloves variables (gloves sold/quater)
firstQuater = 10
secondQuater = 8
thrirdQuater = 5
fourthQuater = 9

# Produce x axis

goto(80, 0)

# Produce y axis

goto(0,0)
goto(0,100)

# Plot data

goto(0,0)
goto(20, firstQuater * 10)
goto(40, secondQuater * 10)
goto(60, thrirdQuater * 10)
goto(80, fourthQuater * 10)

