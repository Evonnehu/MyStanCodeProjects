"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

MY DESCRIPTION HERE:
Make the Attributes, Objects, Methods here for the Python game 'breakout' using.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(window_width-self.ball.width)/2, y=(window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        print(f"{self.__dx},{self.__dy}")

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                # Brick color can be designed better!
                if j < (brick_rows//5)*1:
                    self._brick_color = 'firebrick'
                elif (brick_rows//5)*1 <= j < (brick_rows//5)*2:
                    self._brick_color = 'orange'
                elif (brick_rows//5)*2 <= j < (brick_rows//5)*3:
                    self._brick_color = 'sandybrown'
                elif (brick_rows//5)*3 <= j < (brick_rows//5)*4:
                    self._brick_color = 'green'
                elif (brick_rows//5)*4 <= j:
                    self._brick_color = 'blue'
                self.brick.fill_color = self._brick_color
                self.brick.color = self._brick_color
                self.brick.x = 0 + (brick_width+brick_spacing) * i
                self.brick.y = brick_offset + (brick_height+brick_spacing) * j
                self.window.add(self.brick, x=self.brick.x, y=self.brick.y)

        # Calculate how many bricks for the scores and game winning.
        self.brick_total = brick_cols * brick_rows

        # The Scoreboard
        self._score = 0
        self.scoreboard = GLabel('Score: ' + str(self._score))
        self.scoreboard.font = 'Impact-20'
        self.window.add(self.scoreboard, x=0, y=0+self.scoreboard.height)

        # The switch of the game.
        self.is_start = False

        # Initialize our mouse listeners
        onmouseclicked(self.game_start)
        onmousemoved(self.paddle_moving)

    def paddle_moving(self, mouse):
        """
        To move the paddle by mouse.
        :param mouse: GmouseEvent, mouse move event.
        """
        paddle_offset = PADDLE_OFFSET
        if mouse.x - self.paddle.width * 0.5 <= 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width * 0.5 >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width * 0.5

        self.paddle.y = self.window.height - paddle_offset

    def game_start(self, event):
        """
        To start the game by setting the ball velocity.
        :param event: GmouseEvent, mouse clicked event.
        """
        if not self.is_start:
            self.is_start = True
            if self.is_start:
                self.set_ball_velocity()
                print(f"{self.__dx}, {self.__dy}")

    def set_ball_velocity(self):
        """
        Sets ball x velocity random negative or positive number.
        Sets ball y velocity to default INITIAL_Y_SPEED.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter for the velocity of the ball
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def check_ball_hit(self):
        """
        Check four corners of the ball whether hit any object or not.
        :return: object, the 1st one hit; or 'None' if nothing hit
        """
        ball_left_top = self.window.get_object_at(x=self.ball.x, y=self.ball.y)
        ball_right_top = self.window.get_object_at(x=self.ball.x+self.ball.width, y=self.ball.y)
        ball_left_bottom = self.window.get_object_at(x=self.ball.x, y=self.ball.y+self.ball.height)
        ball_right_bottom = self.window.get_object_at(x=self.ball.x+self.ball.width, y=self.ball.y+self.ball.height)

        if ball_left_bottom is not None:
            return ball_left_bottom
        elif ball_right_bottom is not None:
            return ball_right_bottom
        elif ball_left_top is not None:
            return ball_left_top
        elif ball_right_top is not None:
            return ball_right_top
        else:
            return None

    def reset_ball(self):
        """
        Reset the ball to the start position with velocity x = 0 and velocity y = 0.
        Also, turn off the switch of the game to False.
        """
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        self.is_start = False
        self.__dx = 0
        self.__dy = 0

    def game_over(self):
        """
        Show the game over screen if the NUM_LIVES = 0.
        """
        screen = GRect(width=self.window.width, height=self.window.height)
        screen.filled = True
        self.window.add(screen)

        label = GLabel('Game Over!')
        label.font = 'Impact-40'
        label.color = 'white'
        self.window.add(label, x=(self.window.width-label.width)/2, y=(self.window.height+label.height)/2)

    def congrats(self):
        """
        Show the game-winning screen if complete hitting all bricks.
        """
        screen = GRect(width=self.window.width, height=self.window.height)
        screen.filled = True
        screen.fill_color = 'ivory'
        self.window.add(screen)

        label = GLabel('You Win!')
        label.font = 'Impact-40'
        label.color = 'crimson'
        self.window.add(label, x=(self.window.width - label.width) / 2, y=(self.window.height + label.height) / 2)









