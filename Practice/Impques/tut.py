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
    #choose the color for your circle
    for color in ('red', 'magenta', 'blue',
                  'cyan', 'green', 'white',
                  'yellow'):
        tt.color(color)
        #drwa circle of your choice choose 100 here
        tt.circle(100)

        #draw crilce after 10 pixels left
        tt.left(10)

    #close or hide the turtle
    tt.hideturtle()
tt.mainloop()

