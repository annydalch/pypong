import sys
import pygame
import pdb
import Paddle_class
import globals

pygame.init()

screen = pygame.display.set_mode(globals.SCREEN_SIZE)
clock = pygame.time.Clock()


player_paddle = Paddle_class.Player_paddle(globals.SCREEN_PADDING,
                                           globals.FOREGROUND_COLOR,
                                           globals.PADDLE_SPEED,
                                           globals.PADDLE_SIZE,)


def update():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
    player_paddle.update()


def draw():
    screen.fill(globals.BACKGROUND_COLOR)
    player_paddle.draw(screen)
    pygame.display.update()



def main():
    while 1:
        update()
        draw()
        clock.tick(globals.MAX_FRAME_RATE)
        pygame.display.set_caption("Pong running at {0} fps".format(clock.get_fps()))
        

main()
