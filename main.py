import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра_ТИР")
icon = pygame.image.load("Images/shooting.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("Images/target.png")
target_width = 100
target_height = 100

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

you_win_img = pygame.image.load("Images/you_win.png")
you_win_width = 100
you_win_height = 100

you_win_x = SCREEN_WIDTH / 2 - you_win_width / 2
you_win_y = SCREEN_HEIGHT / 2 - you_win_height / 2

you_lose_img = pygame.image.load("Images/you_lose.png")
you_lose_width = 100
you_lose_height = 100

you_lose_x = SCREEN_WIDTH / 2 - you_lose_width / 2
you_lose_y = SCREEN_HEIGHT / 2 - you_lose_height / 2

count_target = 0
count_target_win = 5
count_not_target = 0
count_target_lose = 5

running = True
winner = False
game_over = False
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                count_target += 1
                print(f"В цель {count_target}")
                if count_target == count_target_win:
                    winner = True
                    start_time = pygame.time.get_ticks()
            else:
                count_not_target += 1
                print(f"Мимо {count_not_target}")
                if count_not_target == count_target_lose:
                    game_over = True
                    start_time = pygame.time.get_ticks()

    if winner:
        screen.fill(color)
        screen.blit(you_win_img, (you_win_x, you_win_y))
    elif game_over:
        screen.fill(color)
        screen.blit(you_lose_img, (you_lose_x, you_lose_y))
    else:
        screen.blit(target_img, (target_x, target_y))

    pygame.display.update()

    if winner or game_over:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 3000:  
            running = False

pygame.quit()
sys.exit()