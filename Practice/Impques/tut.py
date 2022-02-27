#import the turtle from the library to draw circle

import turtle as tt

#set background color
#set pensize and spped of drawing
#curve as 10(relative)

tt.bgcolor('black')
tt.pensize(2)
tt.speed(11)

#itterate 6 times
for i in range(6):
    for color in ('red','blue','yellow',
                  'pink','green','brown'):
        tt.color(color)
        tt.circle(100)
        tt.left(10)
    tt.hideturtle()
tt.mainloop()