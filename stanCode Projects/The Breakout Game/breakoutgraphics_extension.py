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
from campy.graphics.gimage import GImage

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


class BreakoutGraphicsExtension:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        self.is_bouncing = False

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

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

        # record the score
        self.score = 0
        self.score_label = GLabel('Score:' + str(self.score))
        self.score_label.font = '-10'
        self.window.add(self.score_label, x=0, y=brick_offset / 2)

        self.sticker = GImage('emoji.png')
        self.brick_offset = brick_offset

        # Default initial velocity for the ball

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.paddle_move)

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
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=brick_offset + i * (brick_height + brick_spacing))

    def start_game(self, mouse):
        if not self.is_bouncing:
            self.is_bouncing = True
            self.dx = random.randint(1, MAX_X_SPEED)
            self.dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.dx = -self.dx

    def get_vx(self):
        return self.dx

    def get_vy(self):
        return self.dy

    def ball_bounce(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.dx = - self.dx
        is_collided = False
        for i in range(2):
            for j in range(2):
                maybe_object = self.window.get_object_at(self.ball.x + i * self.ball_radius * 2,
                                                         self.ball.y + j * self.ball_radius * 2)
                if maybe_object is not None:
                    if maybe_object is not self.paddle:
                        self.window.remove(maybe_object)
                        self.dy = - self.dy
                        if self.score != 0 and self.score % 10 == 0:                # when score is a multiple of 10
                            random_x = random.randint(0, self.window_width - self.sticker.width)
                            random_y = random.randint(self.brick_offset,
                                                      self.window_height - self.paddle_offset - self.sticker.height)
                            self.window.add(self.sticker, x=random_x, y=random_y)   # pop up a sticker at random place
                        if maybe_object is self.sticker:                            # if ball touches the sticker
                            self.score -= 3                                         # score -3
                        else:
                            self.score += 1
                        self.score_label.text = 'Score:' + str(self.score)          # update score
                    elif maybe_object is self.paddle or self.sticker:
                        self.ball.y -= 3
                        self.dy = - self.dy
                    is_collided = True
                    break
            if is_collided:
                break

    def reset(self):
        self.window.add(self.ball, x=self.window.width / 2 - self.ball_radius,
                        y=self.window.height / 2 - self.ball_radius)
        self.dx = 0
        self.dy = 0
        self.is_bouncing = False

    def paddle_move(self, mouse):
        self.paddle.x = mouse.x - self.paddle_width / 2
        if self.paddle.x < 0:
            self.paddle.x = 0
        elif self.paddle.x + self.paddle_width > self.window_width:
            self.paddle.x = self.window_width - self.paddle_width
        self.paddle.y = self.window.height - self.paddle_height - self.paddle_offset

    def end_game(self):
        self.window.remove(self.ball)
        game_over = GLabel('GAME OVER ☠')
        game_over.font = '-30-bold'
        game_over.color = 'black'
        self.window.add(game_over, x=(self.window_width - game_over.width) / 2, y=self.window_height / 2)
