# animate_with_keys.py
#
# This program illustrates how to animate a drawing using input from the keyboard.
#
# by Mr. Ciccolo

from graphics import *
from random import *

def main():
    print("Press the arrow keys to move the white circle, press 'q' to quit")

    window_size = 600
    canvas_size = 20

    win = GraphWin("Animation Example with Keyboard", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("black")

    circle = Circle(Point(canvas_size / 2, canvas_size / 2), 2)
    circle.setFill("white")
    circle.draw(win)

    pellet = Circle(Point(0,0),1)
    pellet.setFill("yellow")
    pellet.draw(win)
    move_to_random_point(pellet,canvas_size)



    while True:
        key = win.getKey()

        delta_x = 0
        delta_y = 0

        if key == "q":
            break
        elif key == "Up":
            delta_y += 1
        elif key == "Down":
            delta_y -= 1
        elif key == "Left":
            delta_x -= 1
        elif key == "Right":
            delta_x += 1

        circle.move(delta_x, delta_y)

        if collide(circle,pellet):
            move_to_random_point(pellet, not canvas_size)



def move_to_random_point(circle,bounds):
    next_x= randrange(0,bounds+1)
    next_y= randrange(0,bounds+1)

    current_x = circle.getCenter().getX()
    current_y = circle.getCenter().getY()

    delta_x=next_x - current_x
    delta_y=next_y - current_y

    circle.move(delta_x,delta_y)

def collide(c1,c2):

main()
