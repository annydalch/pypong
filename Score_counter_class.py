import pygame
import globals

pygame.font.init()


class Score_counter:
    def __init__(self, font, size, pos, color):
        self.font = pygame.font.SysFont(font, size)
        self.pos = pos
        self.color = color
        self.score = 0

    def earn_point(self):
        self.score += 1

    def make_text(self):
        text = self.font.render(str(self.score), False, self.color)
        return text

    def reset(self):
        self.score = 0

    def draw(self, display):
        display.blit(self.make_text(), self.pos)
