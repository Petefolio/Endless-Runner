import pygame
import math
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
WIDTH = 1300
HEIGHT = 550
gravity = 1

score = 0
player_x = WIDTH/4
player_y = 410
y_change = 0
x_change = 0

obstacles = [600, 900, 1200]
obstacle_speed = 2
active = False

multipliers = [random.randint(2000, 2500)]
multiplier_speed = 8
score_multiply = False

powerups = [random.randint(1500, 1800)]
have_powerup = False
powerup_speed = 5
jump_counter = 0

timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Infinite Runner')

background = pygame.image.load('bg_sea.png')
background_width = background.get_width()
background = pygame.transform.scale(background, (background_width, HEIGHT))
background_rect = background.get_rect()

speed = 5
scroll = 0
direction = 0
panels = math.ceil(WIDTH / background_width) + 2

running = True
while running: 
    timer.tick(fps)
    for i in range(panels):
        screen.blit(background, (i * background_width + scroll - background_width, 0))

    player = pygame.draw.rect(screen, (255, 255, 0), [player_x, player_y, 50, 50], 5, 8)
    score_text = font.render(f'Score: {score}', True, white, black)
    screen.blit(score_text, (1200, 20))
    obstacle0 = pygame.draw.rect(screen, red, [obstacles[0], 410, 50, 50])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 410, 50, 50])
    obstacle2 = pygame.draw.rect(screen, yellow, [obstacles[2], 410, 50, 50])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_TAB:
                obstacles = [600, 900, 1200]
                player_x = WIDTH/4
                score = 0
                active = True
        
        if jump_counter == 0:
            have_powerup = False
        
        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                if have_powerup == True:
                    y_change = 30
                    jump_counter -= 1
                else:
                    y_change = 20
            if event.key == pygame.K_RIGHT:
                x_change = 2
            if event.key == pygame.K_LEFT:
                x_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0
        
    for i in range(len(powerups)):
        if active and have_powerup == False:
            powerups[i] -= powerup_speed
            if powerups[i] < -20:
                powerups[i] = random.randint(1500, 1800)
            if player.colliderect(powerup):
                jump_counter += 3
                have_powerup = True

    for i in range(len(multipliers)):
        if active and score_multiply == False:
            multipliers[i] -= multiplier_speed
            if multipliers[i] < -20:
                multipliers[i] = random.randint(2000, 2500)
            if player.colliderect(multipler):
                score_multiply = True


    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(1350, 1500)
                score += 1
                if score_multiply:
                    score += 1
                
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False
    
    if 0 <= player_x <= 1250:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 1250:
        player_x = 1250

    if y_change > 0 or player_y < 410:
        player_y -= y_change
        y_change -= gravity 
    if y_change > 410:
        player_y = 410
    if player_y == 410 and y_change < 0:
        y_change = 0

    if score_multiply:
        multipler = pygame.draw.rect(screen, green, [multipliers[0], 410, 20, 20])
        multiplier_speed = 0
        multipliers[0] = random.randint(2000, 2500)
        

    else:
        multipler = pygame.draw.rect(screen, green, [multipliers[0], 410, 20, 20])
        multiplier_speed = 8
    

    if have_powerup:
        powerup = pygame.draw.rect(screen, blue, [powerups[0], 600, 30, 30])
        powerup_speed = 0
        powerups[0] = random.randint(1350, 1500)
        if jump_counter > 0:
            jump_counter_text = font.render(f'Jumps: {jump_counter}', True, white, black)
            screen.blit(jump_counter_text, (100, 20))
    else:
        powerup = pygame.draw.rect(screen, blue, [powerups[0], 200, 30, 30])
        gravity = 1
        powerup_speed = 5
    
    scroll -= 5
    if abs(scroll) > background_width:
        scroll = 0
    if active == False:
        scroll = 0

    pygame.display.flip()
pygame.quit()

