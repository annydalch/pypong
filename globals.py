SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (640, 480)
FOREGROUND_COLOR = WHITE = (255, 255, 255)
BACKGROUND_COLOR = BLACK = (0, 0, 0)
PADDLE_SIZE = (PADDLE_WIDTH, PADDLE_HEIGHT) = (10, 50)
SCREEN_PADDING = 20
PADDLE_SPEED = 10
MAX_FRAME_RATE = 30

ACTIVE_SCREEN_REGION = (SCREEN_L_WITH_PADDING,
                        SCREEN_T_WITH_PADDING,
                        SCREEN_R_WITH_PADDING,
                        SCREEN_B_WITH_PADDING) = (SCREEN_PADDING,
                                                  SCREEN_PADDING,
                                                  SCREEN_WIDTH - SCREEN_PADDING,
                                                  SCREEN_HEIGHT - SCREEN_PADDING)

score = [0, 0]
