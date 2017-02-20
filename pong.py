import sys
import pygame
import Paddle_class
import Ball_class
import globals
import Score_counter_class

pygame.init()

screen = pygame.display.set_mode(globals.SCREEN_SIZE)
clock = pygame.time.Clock()

player_score_count = Score_counter_class.Score_counter("freemono",
                                                       30,
                                                       ((globals.SCREEN_WIDTH / 2) - 30, globals.SCREEN_T_WITH_PADDING + 10),
                                                       globals.FOREGROUND_COLOR)
player_paddle = Paddle_class.Player_paddle(globals.SCREEN_L_WITH_PADDING,
                                           globals.FOREGROUND_COLOR,
                                           globals.PADDLE_SPEED,
                                           globals.PADDLE_SIZE,
                                           player_score_count)

opponent_score_count = Score_counter_class.Score_counter("freemono",
                                                         30,
                                                         ((globals.SCREEN_WIDTH / 2) + 30, globals.SCREEN_T_WITH_PADDING + 10),
                                                         globals.FOREGROUND_COLOR)
opponent_paddle = Paddle_class.Paddle(globals.SCREEN_R_WITH_PADDING - globals.PADDLE_WIDTH,
                                      globals.FOREGROUND_COLOR,
                                      globals.PADDLE_SPEED,
                                      globals.PADDLE_SIZE,
                                      opponent_score_count)

ball = Ball_class.Ball(globals.FOREGROUND_COLOR,
                       6,
                       10,
                       player_score_count,
                       opponent_score_count)


def update():
    for event in pygame.event.get():  # check for quit events
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                sys.exit()
    key_mods = pygame.key.get_pressed()  # store the keyboard state in case it changes during the cycle
    player_paddle.update(key_mods)  # update paddles
    opponent_paddle.update(key_mods)
    ball.update(player_paddle, opponent_paddle)  # update the ball


def draw():  # all my draw methods take screen as an argument so it doesn't have to be in globals.py
    screen.fill(globals.BACKGROUND_COLOR)  # fill with black
    player_paddle.draw(screen)  # draw the player paddle
    opponent_paddle.draw(screen)  # draw the other paddle
    ball.draw(screen)  # draw the ball
    player_score_count.draw(screen)  # draw the player's score
    opponent_score_count.draw(screen)  # draw the opponent's score
    pygame.display.update()  # flip the display


def main():  # one day I will move to having a small external loader that will call main instead of inlining it
    # but really I just feel weird doing things any other way than this
    while 1:
        update()
        draw()
        clock.tick(globals.MAX_FRAME_RATE)  # clock.tick counts frame rate and its optional argument limits to the given frame rate
        pygame.display.set_caption(  # the window title
            "Pong running at {0} fps".format(clock.get_fps())
        )


main()
