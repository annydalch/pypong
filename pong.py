import sys
import pygame
import Paddle_class
import Ball_class
import globals
import random
import Score_counter_class

pygame.init()

screen = pygame.display.set_mode(globals.SCREEN_SIZE)
clock = pygame.time.Clock()

player_score_count = Score_counter_class.Score_counter("freemono", 30, ((globals.SCREEN_WIDTH / 2) - 30, globals.SCREEN_T_WITH_PADDING + 10), globals.FOREGROUND_COLOR)
player_paddle = Paddle_class.Player_paddle(globals.SCREEN_PADDING,
                                           globals.FOREGROUND_COLOR,
                                           globals.PADDLE_SPEED,
                                           globals.PADDLE_SIZE,
                                           player_score_count)


ball = Ball_class.Ball(random.randrange(0, 6),
                       globals.FOREGROUND_COLOR,
                       6,
                       10)

def update():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
    player_paddle.update()
    ball.update()


def draw():
    screen.fill(globals.BACKGROUND_COLOR)
    player_paddle.draw(screen)
    ball.draw(screen)
    player_score_count.draw(screen)
    opponent_score_count.draw(screen)
    pygame.display.update()


def main():
    while 1:
        update()
        draw()
        clock.tick(globals.MAX_FRAME_RATE)
        pygame.display.set_caption(
            "Pong running at {0} fps".format(clock.get_fps())
        )


main()
