import globals
import pygame
import math
import random


class Ball:
    def __init__(self, color, vel, size, left_scorecounter, right_scorecounter):
        # color: color of the ball
        # vel: a float telling how fast it's going
        # size: an int telling how many pixels in diameter it is
        # left/right _scorecounter: scorecounter objects for the left and right
        self.color = color
        self.size = size
        self.vel = vel
        self.score_counters = (left_scorecounter, right_scorecounter)  # I store this as a tuple for no particular reason
        # not taking it as a tuple in the argument is also completely arbitrary
        self.reset_pos()

    def reset_pos(self):
        l_or_r = random.randint(0, 1)  # pick which side you're serving to
        if l_or_r == 0:
            angle = (random.random() - .5) * 2  # gen a random angle -pi/4 < theta < pi/4 (ish)
        else:
            angle = ((random.random() - .5) * 2) + 3.14  # gen a random angle 3pi/4 < theta < 5pi/4 (ish)
        self.pos = [((globals.SCREEN_WIDTH / 2) - (self.size / 2)),  # be in the middle
                    ((globals.SCREEN_HEIGHT / 2) - (self.size / 2))]  # both x- and y-wise
        self.delta = [(self.vel * math.cos(angle)),  # convert angle and stored magnitude to x and y components
                      (self.vel * math.sin(angle))]

    def make_rect(self):
        # returns a nice rectangle for drawing
        return (int(round(self.pos[0])),  # we want to store pos as floats for better movement
                int(round(self.pos[1])),  # but we can't draw at a fraction of a pixel so we round
                self.size,
                self.size)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.make_rect(), 0)  # rectangles are more authentic than circles

    def check_rl_borders(self):
        if (self.pos[0] < globals.SCREEN_L_WITH_PADDING):
            self.score_counters[1].earn_point()
            self.reset_pos()
        elif (self.pos[0] > globals.SCREEN_R_WITH_PADDING):
            self.score_counters[0].earn_point()
            self.reset_pos()

    def move_y(self):
        newy = self.pos[1] + self.delta[1]  # calculate where you'll be after movement
        if not ((newy < globals.SCREEN_T_WITH_PADDING) or  # for the y direction
                (newy + self.size > globals.SCREEN_B_WITH_PADDING)):  # see if newy is a legal position
            self.pos[1] = newy  # if it is, move there
        else:  # otherwise, flip the sign of your dy and move with that instead
            self.delta[1] *= -1
            self.pos[1] += self.delta[1]

    def move_x(self, left_paddle, right_paddle):
        newx = self.pos[0] + self.delta[0]  # calculate where you'll be after movement
        if ((newx < (globals.SCREEN_L_WITH_PADDING + left_paddle.size[0])) and  # these are some dense predicates, but we check if it's hitting
                (((self.pos[1] + self.size) > left_paddle.pos[1]) and  # a paddle x-wise and is between the top and bottom of that paddle y-wise
                 (self.pos[1] < (left_paddle.pos[1] + left_paddle.size[1])))):
            self.delta[0] *= -1  # flip the sign of your dy
            self.pos[0] += self.delta[0]  # use that instad of your old dy for movement
        elif (((newx + self.size) > globals.SCREEN_R_WITH_PADDING) and  # same predicate as above, but swapping the other screen border
                (((self.pos[1] + self.size) > right_paddle.pos[1]) and  # and the other paddle
                 (self.pos[1] < (right_paddle.pos[1] + right_paddle.size[1])))):
            self.delta[0] *= -1  # same as for other side
            self.pos[0] += self.delta[0]
        else:
            self.pos[0] = newx  # if it didn't bounce, move it

    def update(self, left_paddle, right_paddle):
        self.move_y()
        self.move_x(left_paddle, right_paddle)
        self.check_rl_borders()  # this function checks if it's gone off the l/r borders and increments score if it has

