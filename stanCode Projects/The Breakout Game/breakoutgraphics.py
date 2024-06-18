"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Width of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.is_bouncing = False

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window.width - paddle_width) / 2,
                            y=self.window.height - paddle_height - paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2,
                          x=self.window.width / 2 - ball_radius, y=self.window.height / 2 - ball_radius)
        self.ball_radius = ball_radius
        self.ball.filled = True
        self.dx = 0
        self.dy = 0
        self.window.add(self.ball)

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)
        self.num = brick_rows * brick_cols

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.color = 'red'
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.color = 'orange'
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.color = 'yellow'
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.color = 'green'
                    self.brick.fill_color = 'green'
                else:
                    self.brick.color = 'blue'
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, x=j*(brick_width+brick_spacing),
                                y=brick_offset + i*(brick_height+brick_spacing))

    def start_game(self, mouse):                            # click to start
        if not self.is_bouncing:                            # prevent mouse disturbance
            self.is_bouncing = True
            self.dx = random.randint(1, MAX_X_SPEED)        # set velocity
            self.dy = INITIAL_Y_SPEED
            if random.random() > 0.5:                       # set dx direction
                self.dx = -self.dx

    def get_vx(self):                                       # setter and getter
        return self.dx

    def get_vy(self):                                       # setter and getter
        return self.dy

    def ball_bounce(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:  # right and left wall
            self.dx = - self.dx
        is_collided = False                                                         # no collided with brick or paddle
        for i in range(2):
            for j in range(2):
                maybe_object = self.window.get_object_at(self.ball.x + i * self.ball_radius * 2,
                                                         self.ball.y + j * self.ball_radius * 2)
                if maybe_object is not None:                                        # if collided
                    if maybe_object is not self.paddle:                             # if collided with brick
                        self.window.remove(maybe_object)
                        self.num -= 1
                        self.dy = - self.dy
                    elif maybe_object is self.paddle:                               # if collided with paddle
                        self.ball.y -= 3                                            # make it leave paddle
                        self.dy = - self.dy
                    is_collided = True                                              # collision happens
                    break                                                           # leave 'j'
            if is_collided:
                break                                                               # leave 'i'

    def reset(self):
        self.window.add(self.ball, x=self.window.width / 2 - self.ball_radius,      # put a new ball
                        y=self.window.height / 2 - self.ball_radius)
        self.dx = 0
        self.dy = 0
        self.is_bouncing = False                                                    # to make mouse work later

    def paddle_move(self, mouse):                                       # control paddle
        self.paddle.x = mouse.x - self.paddle_width / 2                 # make mouse at the center of paddle
        if self.paddle.x < 0:
            self.paddle.x = 0                                           # show the whole paddle when at left
        elif self.paddle.x + self.paddle_width > self.window_width:     # show the whole paddle when at right
            self.paddle.x = self.window_width - self.paddle_width
        self.paddle.y = self.window.height - self.paddle_height - self.paddle_offset        # height is always the same
