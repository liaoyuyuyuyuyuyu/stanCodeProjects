"""
File: bouncing_ball.py
Name: Zoe
-------------------------
TODO: Simulate a bouncing ball. Make it bounce three times at most.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
is_bouncing = False
window = GWindow(800, 500, title='bouncing_ball.py')
time = 0
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global is_bouncing, ball, time
    onmouseclicked(bounce)
    while True:
        pause(DELAY)
        if time < 3:                                    # drop the ball 3 times at most
            if is_bouncing:
                ver = 0                                 # the vertical speed
                while ball.x < window.width:            # when bounce in the window
                    ver += GRAVITY                      # vertical speed + gravity => faster
                    ball.move(VX, ver)
                    pause(DELAY)
                    if ball.y > window.height:          # when ball hits the floor
                        ver = -ver * REDUCE             # make ball rebound
                        ball.move(VX, ver)
                        pause(DELAY)
                is_bouncing = False
                window.add(ball, x=START_X, y=START_Y)
                time += 1                               # record times of drop
        else:
            break


def bounce(mouse):
    global is_bouncing
    if not is_bouncing:
        is_bouncing = True


if __name__ == "__main__":
    main()
