import pygame
import random

# setting up the screen and whatnot

# constants for the window width and height
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720

# the RGB values for the colors used
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


def main():
    # Game setup

    # initializing the pygame library 
    pygame.init()

    # creating a window for the game
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # set the window's title
    pygame.display.set_caption("Pong")

    # main code for having the ball move
    clock = pygame.time.Clock()  # to track the ball movement timing

    started = False  # for the "Press Space to Start" screen

    # setting up the players and the ball 

    # paddle 1 (left player)
    paddle_1_rect = pygame.Rect(30, SCREEN_HEIGHT // 2 - 50, 7, 100)

    # paddle 2 (right player)
    paddle_2_rect = pygame.Rect(SCREEN_WIDTH - 37, SCREEN_HEIGHT // 2 - 50, 7, 100)

    # tracking how much each player moves
    paddle_1_move = 0
    paddle_2_move = 0

    # rectangle that represents the ball 
    ball_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 25, 25)

    # determine the x and y direction of where the ball will go 
    ball_accel_x = random.choice([-0.3, 0.3])
    ball_accel_y = random.choice([-0.3, 0.3])

    # game loop
    while True:

        # setting up the background color and the overall vibes of the game
        screen.fill(COLOR_BLACK)

        # starting screen until space is pressed
        if not started:
            # load the Consolas font
            font = pygame.font.SysFont('Consolas', 30)

            # draw some text to the center of the screen
            text = font.render('Press SPACE to Start', True, COLOR_WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

            # update the display
            pygame.display.flip()

            # listen for events during the start screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # closing the window
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # start the game
                        started = True
            continue  # skip the rest of the loop until game starts

        # get the time elapsed between now and the last frame
        delta_time = clock.tick(60)

        # checking for events
        for event in pygame.event.get():

            # if user exits the window
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # if user is pressing a key
            if event.type == pygame.KEYDOWN:

                # player 1 controls (left)
                if event.key == pygame.K_w:
                    paddle_1_move = -0.5  # move up
                if event.key == pygame.K_s:
                    paddle_1_move = 0.5   # move down

                # player 2 controls (right)
                if event.key == pygame.K_UP:
                    paddle_2_move = -0.5
                if event.key == pygame.K_DOWN:
                    paddle_2_move = 0.5

            # player released a key
            if event.type == pygame.KEYUP:

                # stop paddle 1 movement
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle_1_move = 0

                # stop paddle 2 movement
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle_2_move = 0

        # move the paddles according to the movement variables
        paddle_1_rect.y += paddle_1_move * delta_time
        paddle_2_rect.y += paddle_2_move * delta_time

        # stop paddles from going off-screen
        paddle_1_rect.clamp_ip(screen.get_rect())
        paddle_2_rect.clamp_ip(screen.get_rect())

        # move the ball
        ball_rect.x += ball_accel_x * delta_time
        ball_rect.y += ball_accel_y * delta_time

        # if the ball hits the top or bottom, invert its vertical speed
        if ball_rect.top <= 0 or ball_rect.bottom >= SCREEN_HEIGHT:
            ball_accel_y *= -1

        # if the ball collides with the paddles, bounce it
        if paddle_1_rect.colliderect(ball_rect) or paddle_2_rect.colliderect(ball_rect):
            ball_accel_x *= -1

        # if the ball goes out of bounds, end the game
        if started: 

            if ball_rect.left <= 0 or ball_rect.right >= SCREEN_WIDTH:
                pygame.quit()
                return
            
        if paddle_1_rect.top < 0:
            paddle_1_rect.top = 0
        if paddle_1_rect.bottom > SCREEN_HEIGHT:
            paddle_1_rect.bottom = SCREEN_HEIGHT

        if paddle_2_rect.top < 0:
            paddle_2_rect.top = 0
        if paddle_2_rect.bottom > SCREEN_HEIGHT:
            paddle_2_rect.bottom = SCREEN_HEIGHT

        # draw player 1 and 2 paddles
        pygame.draw.rect(screen, COLOR_WHITE, paddle_1_rect)
        pygame.draw.rect(screen, COLOR_WHITE, paddle_2_rect)

        # drawing the ball with the white color
        pygame.draw.rect(screen, COLOR_WHITE, ball_rect)

        # update the display
        pygame.display.update()


# run the game
if __name__ == "__main__":
    main()
