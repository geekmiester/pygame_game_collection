import pygame
pygame.init()

# Set up the game window
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Arrow Control Game")

# Set up the player
player_size = 50
player_position = [window_size[0]//2, window_size[1]//2]

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        # Move the player using arrow controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_position[0] -= 10
            elif event.key == pygame.K_RIGHT:
                player_position[0] += 10
            elif event.key == pygame.K_UP:
                player_position[1] -= 10
            elif event.key == pygame.K_DOWN:
                player_position[1] += 10
    
    # Draw the player on the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (player_position[0], player_position[1], player_size, player_size))
    
    # Update the screen
    pygame.display.update()
    
    # Set the game clock speed
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
