"""
write a code to draw the shape of hexagon
"""

import turtle

turtle.screensize()
a = turtle.Turtle()

for i in range(6):
    a.forward(100)
    a.left(60)
turtle.mainloop()