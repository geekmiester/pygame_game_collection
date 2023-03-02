import pygame
import random

pygame.init()
pygame.mixer.init()

# screen size
screen = pygame.display.set_mode((600, 600))

# title of the window
pygame.display.set_caption("Space adventures")

# clock to control game speed
clock = pygame.time.Clock()

# player image
player_image = pygame.image.load("player.png")
player_rect = player_image.get_rect()

# obstacle image
obstacle_image = pygame.image.load("asteroid.png")
obstacle_rect = obstacle_image.get_rect()

# Initialize player position
player_rect.x = 300
player_rect.y = 550

# Initialize obstacle list
obstacles = []
for i in range(20):
    obstacle = obstacle_image.get_rect()
    obstacle.x = random.randint(0, 600)
    obstacle.y = random.randint(-600, -100)
    obstacles.append(obstacle)

# Initialize obstacle speed
obstacle_speed = 3

# Initialize score
score = 0

# Game loop
game_over=False
running = False
while not running:

   
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
        elif event.type == pygame.K_SPACE:
            game_over = True
            running=False
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    final_score=0

    if not game_over:
        
    #Play music
        # pygame.mixer.music.load("space.mp3")
        pygame.mixer.music.load("space.wav")
        pygame.mixer.music.play(loops=-1)
        
    # Move obstacles down
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
        
        # Check if obstacle reached the bottom of the screen
        for obstacle in obstacles:
            if obstacle.y >= 600:
                obstacle.x = random.randint(0, 550)
                obstacle.y = random.randint(-600, -100)
                score += 1
        
        # Clear the screen
        screen.fill((0,0,0))
        
        # Draw player
        screen.blit(player_image, player_rect)
        
        # Draw obstacles
        for obstacle in obstacles:
            screen.blit(obstacle_image, obstacle)
        
        # Display score
        font = pygame.font.Font(None, 30)

        score_text = font.render("Score: " + str(score), True, (255,255,255))
        screen.blit(score_text, (450, 10))
        
    # Check if player hit the obstacle
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle):
                screen.fill((0, 0, 0))
                final_score=score      
                font = pygame.font.Font(None, 30) 
                game_over = font.render("Game Over!! your score  :" + str(final_score),True, (255,255,255))
                screen.blit(game_over, (100, 200))
                pygame.display.update()


        # Update the screen
        pygame.display.update()
        
        # Set game speed
        clock.tick(60)

        pygame.display.flip()

# Quit pygame
pygame.quit()