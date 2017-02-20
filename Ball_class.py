import globals
import pygame
import math
import random


class Ball:
    def __init__(self, color, vel, size, left_scorecounter, right_scorecounter):
        # angle in radians
        # color of the ball
        # a float telling how fast it's going
        # an int telling how many pixels in diameter it is
        self.color = color
        self.size = size
        self.vel = vel
        self.score_counters = (left_scorecounter, right_scorecounter)
        self.reset_pos()

    def reset_pos(self):
        l_or_r = random.randint(0, 1)
        if l_or_r == 0:
            angle = (random.random() - .5) * 2
        else:
            angle = ((random.random() - .5) * 2) + 3.14
        self.pos = [((globals.SCREEN_WIDTH / 2) - (self.size / 2)),
                    ((globals.SCREEN_HEIGHT / 2) - (self.size / 2))]
        self.delta = [(self.vel * math.cos(angle)),
                      (self.vel * math.sin(angle))]

    def make_rect(self):
        # returns a nice rectangle for drawing
        return (int(round(self.pos[0])),
                int(round(self.pos[1])),
                self.size,
                self.size)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.make_rect(), 0)

    def check_rl_borders(self):
        if (self.pos[0] < globals.SCREEN_L_WITH_PADDING):
            self.score_counters[1].earn_point()
            self.reset_pos()
        elif (self.pos[0] > globals.SCREEN_R_WITH_PADDING):
            self.score_counters[0].earn_point()
            self.reset_pos()

    def move(self):
        newy = self.pos[1] + self.delta[1]  # calculate where you'll be after movement
        
        if not ((newy < globals.SCREEN_T_WITH_PADDING) or  # for the y direction
                (newy + self.size > globals.SCREEN_B_WITH_PADDING)):  # see if newy is a legal position
            self.pos[1] = newy  # if it is, move there
        else:  # otherwise, flip the sign of your dy and move with that instead
            self.delta[1] *= -1
            self.pos[1] += self.delta[1]
        self.pos[0] += self.delta[0]
        self.check_rl_borders()

    def update(self):
        self.move()
        
