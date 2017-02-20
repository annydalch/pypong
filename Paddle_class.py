import pygame
import globals


class Paddle:
    def __init__(self, column, color, speed, size, score_counter):
        self.size = size
        self.pos = [column, (globals.SCREEN_HEIGHT / 2) - (size[1] / 2)]
        self.speed = speed
        self.color = color
        self.score_counter = score_counter
        score_counter.reset()

    def make_rect(self):
        return (self.pos[0], self.pos[1], self.size[0], self.size[1])

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.make_rect(), 0)

    def move(self, dy):
        self.pos[1] += dy

    def update(self):
        return False


class Player_paddle(Paddle):
    def update(self):
        key_mods = pygame.key.get_pressed()
        if key_mods[pygame.K_w] and (not key_mods[pygame.K_s]) and (not self.pos[1] < globals.SCREEN_T_WITH_PADDING):
            self.move(-self.speed)
        if key_mods[pygame.K_s] and (not key_mods[pygame.K_w]) and (not (self.pos[1] + self.size[1]) > (globals.SCREEN_B_WITH_PADDING)):
            self.move(self.speed)
