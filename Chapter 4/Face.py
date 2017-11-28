from graphics import *


def main():

    size = eval(input("How big do you want to make the window? "))

    win = GraphWin("Face Drawing", size, size)
    win.setCoords(400,400, 0, 0)

    # Here's where I will draw the face!
    center = Point (195 , 172)
    circ = Circle(center, 175)
    circ.setFill('orange')
    circ.draw(win)

    center = Point (100, 95)
    circ = Circle(center, 30)
    circ.setFill(color_rgb(30, 243, 129))
    circ.draw(win)

    center = Point (100, 95)
    circ = Circle(center, 15)
    circ.setFill('black')
    circ.draw(win)

    # this is the right eye
    center = Point (300, 95)
    circ = Circle(center, 30)
    circ.setFill(color_rgb(240, 115, 249))
    circ.draw(win)

    center = Point (300, 95)
    circ = Circle(center, 15)
    circ.setFill('black')
    circ.draw(win)

    rectangle = Rectangle (Point(50,240) , Point(350 , 245))
    rectangle.draw(win)
    rectangle.setFill('cyan')

    line = Line (Point(255,300) , Point(155 , 300))
    line.draw(win)
    line.setFill('cyan')

    line = Line (Point(50,245) , Point(155,300))
    line.draw(win)
    line.setFill('cyan')

    line = Line (Point(350,245) , Point(255,300))
    line.draw(win)
    line.setFill('cyan')

    line = Line (Point(150,40) , Point (100,40))
    line.draw(win)
    line.setFill('black')

    line = Line (Point(250,40) , Point (300,40))
    line.draw(win)
    line.setFill('black')

    polygon = Polygon (Point(225,180) , Point(150, 180) , Point(185, 140))
    polygon.draw(win)
    polygon.setFill('blue')


    input("press any key to quit")


main()
