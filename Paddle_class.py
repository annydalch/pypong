import pygame
import globals


class Paddle:
    def __init__(self, column, color, speed, size, score_counter):
        # column: x-po
        # color: what color it is
        # speed: an int telling how fast it can move
        # size: a tuple contaning width and height in px
        # score_counter: a score_counter object associated with this player
        self.size = size
        self.pos = [column, (globals.SCREEN_HEIGHT / 2) - (size[1] / 2)]  # start in the middle y-wise
        self.speed = speed
        self.color = color
        self.score_counter = score_counter
        score_counter.reset()  # reset the score. this is so we can use the same scorecounter for several paddles if we gen new ones with new ai

    def make_rect(self):  # returns a nice rect for drawing
        return (self.pos[0], self.pos[1], self.size[0], self.size[1])

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.make_rect(), 0)

    def move(self, dy):  # this is kinda a silly function
        self.pos[1] += dy

    def update(self, key_mods):  # this parent class doesn't have an update method, so we return False
        return False


class Player_paddle(Paddle):  # the class for the player's left paddle
    # future improvements: take keys as arguments during creation
    # to allow having 2-player or customizable keys
    def update(self, key_mods):
        if key_mods[pygame.K_w] and (not key_mods[pygame.K_s]) and (not self.pos[1] < globals.SCREEN_T_WITH_PADDING):
            # a dense predicate. check if w is pressed, s is not, and you're within the screen
            self.move(-self.speed)
        if key_mods[pygame.K_s] and (not key_mods[pygame.K_w]) and (not (self.pos[1] + self.size[1]) > (globals.SCREEN_B_WITH_PADDING)):
            # same as the above predicate, but for s, w, and the bottom
            self.move(self.speed)
