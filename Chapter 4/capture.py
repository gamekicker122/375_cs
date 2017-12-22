# capture_the_pellets.py
#
# In this program you chase a pellet and everytime 8 seconds or so a power pellet will appear for a few seconds allowing
#you to get a +5 points.I changed the text colors,backrounds and the color of the pellets, I also added a text
#in the backround that says Capture the pellets! which switches to GAMEOVER when the timer runs out.

from graphics import *
from math import *
from random import *


def main():
    print("Press the arrow keys to move the white ball and capture the yellow pellets. Press 'q' to quit.")

    score = 0
    timer = 60
    power_pellet = 5
    power_pellet_visible = False


    window_size = 600
    canvas_size = 20

    win = GraphWin("Capture the Pellets!", window_size, window_size)
    win.setCoords(0, 0, canvas_size, canvas_size)
    win.setBackground("green")

    score_text = Text(Point(0.2 * canvas_size, 0.9 * canvas_size), "Score: " + str(score))
    score_text.setTextColor("blue")
    score_text.setFace("courier")
    score_text.setSize(24)
    score_text.draw(win)

    timer_text = Text(Point(0.7 * canvas_size, 0.9 * canvas_size), "Time: " + str(timer))
    timer_text.setTextColor("blue")
    timer_text.setFace("courier")
    timer_text.setSize(24)
    timer_text.draw(win)

    message_text = Text(Point(canvas_size / 2, canvas_size / 2), "CLICK TO START")
    message_text.setTextColor("black")
    message_text.setFace("courier")
    message_text.setSize(36)
    message_text.draw(win)

    win.getMouse()
    message_text.setText("")

#I added capture the pellets! to the backround and then when the game is over it switches to GAME OVER

    message_text = Text(Point(canvas_size/ 2, canvas_size / 2), "Capture the Pellets!")
    message_text.setTextColor("black")
    message_text.setFace("courier")
    message_text.setSize(36)
    message_text.draw(win)
    ball = Circle(Point(canvas_size / 2, canvas_size / 2), 2)
    ball.setFill("purple")
    ball.draw(win)

    pellet = Circle(Point(0, 0), 1)
    pellet.setFill("yellow")
    pellet.draw(win)
    move_to_random_point(pellet, canvas_size)

    power_pellet = Circle(Point(-10,-10),1)
    power_pellet.setFill("blue")
    power_pellet.draw(win)



    time_check = time.time()
    while timer > 0:
        key = win.checkKey()

        delta_x = 0
        delta_y = 0

        if key == "q":
            break
        elif key == "Up":
            delta_y = 1
        elif key == "Down":
            delta_y = -1
        elif key == "Left":
            delta_x = -1
        elif key == "Right":
            delta_x = 1

        ball.move(delta_x, delta_y)

        if collide(ball, pellet):
            score += 1
            score_text.setText("Score: " + str(score))
            move_to_random_point(pellet, canvas_size)

        if (time.time() - time_check) > 1:
            time_check = time.time()
            timer -= 1
            timer_text.setText("Time: " + str(timer))


        if collide(ball, power_pellet):
            score += 5
            score_text.setText("Score: " + str(score))
            move_off_screen(power_pellet)




        if not power_pellet_visible:
            if randrange(1,300)==1:
                move_to_random_point(power_pellet, canvas_size)
                power_pellet_visible = True

        else:
            if randrange(1,300)==1:
                move_off_screen(power_pellet)
                power_pellet_visible = False

        if timer == 59:
            message_text.setText("")




    message_text.setTextColor("black")
    message_text.setText("GAME OVER")

    input("Game over! Your final score was " + str(score) + ". Press Enter to quit.")


def collide(c1, c2):
    # Calculate the distance between the center points of the circles using Pythagorean theorem (a^2 + b^2 = c^2)
    a = c1.getCenter().getX() - c2.getCenter().getX()
    b = c1.getCenter().getY() - c2.getCenter().getY()
    distance = sqrt(a**2 + b**2)

    collision = distance <= (c1.getRadius() + c2.getRadius())

    return collision


def move_off_screen(circle):
    current_x = circle.getCenter().getX()
    current_y = circle.getCenter().getY()

    next_x = -10
    next_y = -10

    delta_x = next_x - current_x
    delta_y = next_y - current_y

    circle.move(delta_x, delta_y)


def move_to_random_point(circle, bounds):
    current_x = circle.getCenter().getX()
    current_y = circle.getCenter().getY()

    next_x = randrange(circle.getRadius(), bounds + 1 - circle.getRadius())
    next_y = randrange(circle.getRadius(), bounds + 1 - circle.getRadius())

    delta_x = next_x - current_x
    delta_y = next_y - current_y

    circle.move(delta_x, delta_y)






main()
