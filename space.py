import pygame
import random

# initialize Pygame
pygame.init()

# set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GAME_WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

# set up the game clock
clock = pygame.time.Clock()

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set up the spaceship
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 60
spaceship_image = pygame.image.load("player.png").convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
spaceship_x = WINDOW_WIDTH // 2 - SPACESHIP_WIDTH // 2
spaceship_y = WINDOW_HEIGHT - SPACESHIP_HEIGHT - 10
SPACESHIP_SPEED = 5
SPACESHIP_LASER_DAMAGE = 1

# set up the lasers
LASER_WIDTH = 10
LASER_HEIGHT = 30
LASER_COLOR = (255, 0, 0)
lasers = []
LASER_SPEED = 10

# set up the enemy spaceships
ENEMY_SPACESHIP_WIDTH = 60
ENEMY_SPACESHIP_HEIGHT = 40
enemy_spaceships = []
ENEMY_SPACESHIP_SPEED = 5
ENEMY_SPACESHIP_LASER_DAMAGE = 1
ENEMY_SPAWN_RATE = 60

# set up the score
score = 0
font = pygame.font.Font(None, 36)

# main game loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # shoot a laser
                laser_x = spaceship_x + SPACESHIP_WIDTH // 2 - LASER_WIDTH // 2
                laser_y = spaceship_y - LASER_HEIGHT
                lasers.append(pygame.Rect(laser_x, laser_y, LASER_WIDTH, LASER_HEIGHT))

    # update the spaceship position
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= SPACESHIP_SPEED
    if keys[pygame.K_RIGHT] and spaceship_x < WINDOW_WIDTH - SPACESHIP_WIDTH:
        spaceship_x += SPACESHIP_SPEED

    # update the lasers
    for laser in lasers:
        laser.y -= LASER_SPEED
        if laser.y < 0:
            lasers.remove(laser)

    # spawn enemy spaceships
    if random.randint(1, ENEMY_SPAWN_RATE) == 1:
        enemy_spaceship_image = pygame.image.load("meteorite.png").convert_alpha()
        enemy_spaceship_image = pygame.transform.scale(enemy_spaceship_image, (ENEMY_SPACESHIP_WIDTH, ENEMY_SPACESHIP_HEIGHT))
        enemy_spaceship_x = random.randint(0, WINDOW_WIDTH - ENEMY_SPACESHIP_WIDTH)
        enemy_spaceship_y = 0
        enemy_spaceships.append(pygame.Rect(enemy_spaceship_x, enemy_spaceship_y, ENEMY_SPACESHIP_WIDTH, ENEMY_SPACESHIP_HEIGHT))

    # update the enemy spaceships
    for enemy_spaceship in enemy_spaceships:
        enemy_spaceship.y += ENEMY_SPACESHIP_SPEED
