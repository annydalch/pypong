import globals
import pygame
import math


class Ball:
    def __init__(self, angle, color, vel, size):
        # angle in radians
        # color of the ball
        # a float telling how fast it's going
        # an int telling how many pixels in diameter it is
        self.delta = [(vel * math.cos(angle)),  # we convert angle and vel into dx and dy
                      (vel * math.sin(angle))]  # immediately and store them as floats
        self.color = color
        self.size = size
        self.pos = [((globals.SCREEN_WIDTH / 2) - (size / 2)),  # stick it in the middle both x-wise and y-wise
                    ((globals.SCREEN_HEIGHT / 2) - (size / 2))]  # position is floats but make_rect rounds them for drawing

    def make_rect(self):
        # returns a nice rectangle for drawing
        return (int(round(self.pos[0])),
                int(round(self.pos[1])),
                self.size,
                self.size)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.make_rect(), 0)

    def move(self):
        newx = self.pos[0] + self.delta[0]  # calculate where you'll be after movement
        newy = self.pos[1] + self.delta[1]
        if not ((newx < globals.SCREEN_L_WITH_PADDING) or
                (newx + self.size > globals.SCREEN_R_WITH_PADDING)):  # for the x direction, if it's a legal position, move there
            self.pos[0] = newx
        else:  # otherwise, flip the sign of your dx and move where that puts you instead
            self.delta[0] *= -1
            self.pos[0] += self.delta[0]
        
        if not ((newy < globals.SCREEN_T_WITH_PADDING) or  # for the y direction
                (newy + self.size > globals.SCREEN_B_WITH_PADDING)):  # see if newy is a legal position
            self.pos[1] = newy  # if it is, move there
        else:  # otherwise, flip the sign of your dy and move with that instead
            self.delta[1] *= -1
            self.pos[1] += self.delta[1]

    def update(self):
        self.move()
        
