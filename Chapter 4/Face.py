from graphics import *


def main():
    win = GraphWin("Face Drawing", 400, 400)

    # Here's where I will draw the face!
    center = Point (100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)

    # this is the right eye
    center = Point (300, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)


    rectangle = Rectangle (Point(50,210) , Point(350 , 250))
    rectangle.draw(win)
    rectangle.setFill('red')
    input("press any key to quit")


main()
