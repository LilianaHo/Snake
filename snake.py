# Snake game on pygame

import random
import pygame
pygame.init()
pygame.display.set_caption('Snake made by lily')


def display():
    screen.fill((20, 20, 20))
    food = pygame.Rect(food_location[0] * amplification, food_location[1] * amplification, amplification,
                       amplification)
    pygame.draw.rect(screen, (255, 0, 0), food)
    snake_head = pygame.Rect(snake_location[0] * amplification, snake_location[1] * amplification, amplification,
                             amplification)
    pygame.draw.rect(screen, (255, 255, 255), snake_head)

    if len(snake_tail) > 0:
        if len(snake_tail) == 1:
            tail = pygame.Rect(snake_tail[0][0] * amplification, snake_tail[0][1] * amplification, amplification,
                               amplification)
            pygame.draw.rect(screen, (255, 255, 255), tail)
        else:
            for i in range(0, len(snake_tail)):
                tail = pygame.Rect(snake_tail[i][0] * amplification, snake_tail[i][1] * amplification, amplification,
                                   amplification)
                pygame.draw.rect(screen, (255, 255, 255), tail)


# values for actual game, can be amplified depending on how big the screen should be
game_width = 50
game_length = 50
amplification = 10
high_score = 0
new_high_score = False
snake_location = [game_width//2, game_length//2]
snake_tail_length = 0
snake_tail = []
snake_travel_history = []
# can either be up, down, left or right
facing = "up"

food_location = [random.randrange(0, game_width), random.randrange(0,game_length)]


# game window
SCREEN_WIDTH = game_width * amplification
SCREEN_LENGTH = game_length * amplification
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_LENGTH])
# background
screen.fill((20, 20, 20))

# drawing the snake
snake_head = pygame.Rect(snake_location[0] * amplification, snake_location[1] * amplification, amplification, amplification)
pygame.draw.rect(screen, (255, 255, 255), snake_head)

# drawing the food
food = pygame.Rect(food_location[0] * amplification, food_location[1] * amplification, amplification, amplification)
pygame.draw.rect(screen, (255, 0, 0), food)


font = pygame.font.Font("Pixeboy-z8XGD.ttf", 100)
text = font.render("Snake", True, (255, 0, 255))
tiny_font = pygame.font.Font("Pixeboy-z8XGD.ttf", 36)
tiny_text = tiny_font.render("press t to play", True, (255, 0, 255))
high_score_font = pygame.font.Font("Pixeboy-z8XGD.ttf", 36)

# snake game
running = True
game_over = True
while running:
    screen.blit(text, (SCREEN_WIDTH // 2 - 112, SCREEN_LENGTH // 2 - 100))
    screen.blit(tiny_text, (SCREEN_WIDTH // 2 - 105, SCREEN_LENGTH // 2 + 100))
    high_score_colour = 100, 0, 100
    if new_high_score is True:
        high_score_colour = 0, 255, 0
    high_score_text = high_score_font.render("HIGH SCORE: " + str(high_score), True, high_score_colour)
    screen.blit(high_score_text, (5, SCREEN_LENGTH - 25))

    pygame.display.update()
    button = pygame.key.get_pressed()
    if button[pygame.K_t]:
        snake_location = [game_width // 2, game_length // 2]
        snake_tail_length = 0
        snake_tail = []
        snake_travel_history = []
        # can either be up, down, left or right
        facing = "up"

        food_location = [random.randrange(0, game_width), random.randrange(0, game_length)]

        # background
        screen.fill((20, 20, 20))
        # drawing the snake
        snake_head = pygame.Rect(snake_location[0] * amplification, snake_location[1] * amplification, amplification,
                                 amplification)
        pygame.draw.rect(screen, (255, 255, 255), snake_head)
        # drawing the food
        food = pygame.Rect(food_location[0] * amplification, food_location[1] * amplification, amplification,
                           amplification)
        pygame.draw.rect(screen, (255, 0, 0), food)

        game_over = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            running = False
    while game_over is False:
        button = pygame.key.get_pressed()
        if button[pygame.K_w] and facing != "down":
            facing = "up"
        elif button[pygame.K_s] and facing != "up":
            facing = "down"
        elif button[pygame.K_a] and facing != "right":
            facing = "left"
        elif button[pygame.K_d] and facing != "left":
            facing = "right"

        if facing == "up":
            snake_location[1] = snake_location[1] - 1
        if facing == "down":
            snake_location[1] = snake_location[1] + 1
        if facing == "left":
            snake_location[0] = snake_location[0] - 1
        if facing == "right":
            snake_location[0] = snake_location[0] + 1

        if snake_location in snake_tail:
            game_over = True
            if high_score < snake_tail_length:
                high_score = snake_tail_length
                new_high_score = True
        if snake_location[0] >= game_width - 1 or snake_location[0] < 0 or snake_location[1] >= game_length - 1 or snake_location[1] < 0:
            game_over = True
            if high_score < snake_tail_length:
                high_score = snake_tail_length
                new_high_score = True

        if snake_tail_length > 0:
            snake_tail = snake_travel_history[len(snake_travel_history) - snake_tail_length:]
        snake_travel_history.append([snake_location[0], snake_location[1]])

        if snake_location == food_location:
            snake_tail_length += 1
            food_location = [random.randrange(0, game_width), random.randrange(0, game_length)]

        # visuals
        display()

        # exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                running = False

        pygame.display.update()
        pygame.time.wait(100)
# quitting
pygame.quit()
