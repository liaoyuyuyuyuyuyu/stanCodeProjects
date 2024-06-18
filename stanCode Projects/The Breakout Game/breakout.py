"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():

    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        # Check
        if lives > 0:
            # Update
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            graphics.ball.move(vx, vy)
            graphics.ball_bounce()
            if graphics.ball.y > graphics.window.height or graphics.ball.y <= 0:        # when the ball drops
                graphics.reset()
                lives -= 1
            if graphics.num == 0:
                break
        else:
            break


if __name__ == '__main__':
    main()
