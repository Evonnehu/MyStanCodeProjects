"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

MY DESCRIPTION HERE:
This program plays a Python game 'breakout'
A ball will be bouncing in the GWindow, and Players control the paddle by mouse to break all bricks to win the game.
The ball will start at the middle of the GWindow and the game will start when Players click.
Players must well control the paddle to avoid the ball falling, Players only have NUM_LIVES chance to play the game.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# Global variables
vx = 0
vy = 0


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    hit_object_total = 0

    # Animation loop starts from here!
    while True:
        global vx, vy
        # The program will wait for the mouse clicked event to change the ball velocity
        if vx == 0 and vy == 0:
            vx = graphics.get_dx()
            vy = graphics.get_dy()

        # Update
        graphics.ball.move(vx, vy)

        # Check_1: If the ball is outbound.
        if graphics.ball.y > graphics.window.height:
            live -= 1
            if live > 0:
                graphics.reset_ball()
                vy = graphics.get_dx()
                vx = graphics.get_dy()
            else:
                break

        # Check_2: If ball hits bricks or paddle.
        hit_object = graphics.check_ball_hit()

        if hit_object is not None:
            # If hit the paddle and the ball direction is downward.
            if hit_object is graphics.paddle and vy > 0:
                vy = -vy
            # If hit the brick and the ball direction is downward.
            elif hit_object is not graphics.paddle and hit_object is not graphics.scoreboard:
                graphics.window.remove(hit_object)
                hit_object_total += 1
                graphics.scoreboard.text = 'Score: ' + str(hit_object_total)
                vy = -vy
                if hit_object_total == graphics.brick_total:
                    break

        # Check_3: Set the window boundary if the ball hits nothing.
        elif graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx = -vx
        elif graphics.ball.y <= 0:
            vy = -vy

        # Pause
        pause(FRAME_RATE)

    # Lose the game
    if live == 0:
        graphics.game_over()

    # Win the game
    else:
        graphics.congrats()


if __name__ == '__main__':
    main()
