import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 1000
PLAYER_SIZE = 50
ENEMY_SIZE = 30
WEAPON_SIZE = 10
WHITE = (255, 255, 255)
FPS = 60

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player.png')  
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('metorite.png')  
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(0, HEIGHT - ENEMY_SIZE)
        self.speed = random.randint(2, 6)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = WIDTH
            self.rect.y = random.randint(0, HEIGHT - ENEMY_SIZE)
            self.speed = random.randint(2, 6)

# Weapon class
class Weapon(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        self.image = pygame.Surface((WEAPON_SIZE, WEAPON_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = player_rect.centerx
        self.rect.centery = player_rect.centery
        self.speed = 8

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > WIDTH:
            self.kill()
# Start screen
def show_start_screen(screen):
    font_title = pygame.font.Font(None, 74)
    text_title = font_title.render("Platform Game", True, WHITE)
    screen.blit(text_title, (WIDTH // 4, HEIGHT // 4))

    font_button = pygame.font.Font(None, 36)

    start_button = pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2, WIDTH // 2, HEIGHT // 8))
    start_text = font_button.render("Start Game", True, (0, 0, 0))
    screen.blit(start_text, (WIDTH // 3, HEIGHT // 2 + HEIGHT // 32))

    instructions_button = pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2 + HEIGHT // 8 + 10, WIDTH // 2, HEIGHT // 8))
    instructions_text = font_button.render("Instructions", True, (0, 0, 0))
    screen.blit(instructions_text, (WIDTH // 3, HEIGHT // 2 + HEIGHT // 8 + 10 + HEIGHT // 32))

    quit_button = pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2 + 2 * (HEIGHT // 8) + 20, WIDTH // 2, HEIGHT // 8))
    quit_text = font_button.render("Quit Game", True, (0, 0, 0))
    screen.blit(quit_text, (WIDTH // 3, HEIGHT // 2 + 2 * (HEIGHT // 8) + 20 + HEIGHT // 32))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_button.collidepoint(event.pos):
                    return
                elif instructions_button.collidepoint(event.pos):
                    show_instructions(screen)
                elif quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Instructions screen
def show_instructions(screen):
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    instructions_text = font.render("Instructions:" '\n'
                                   "Use arrow keys to move the player.\n"
                                   "Press Space to shoot weapons.\n"
                                   "Press P to pause or resume the game.\n"
                                   "Press Q to quit the game.", True, WHITE)
    screen.blit(instructions_text, (WIDTH // 4, HEIGHT // 4))

    back_button = pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2 + HEIGHT // 4, WIDTH // 2, HEIGHT // 8))
    back_text = font.render("Back to Start", True, (0, 0, 0))
    screen.blit(back_text, (WIDTH // 3, HEIGHT // 2 + HEIGHT // 2 + HEIGHT // 32))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button.collidepoint(event.pos):
                    return

# End screen
def show_end_screen(screen, score):
    screen.fill((0, 0, 0))

    font = pygame.font.Font(None, 36)
    game_over_text = font.render(f"Game Over. Your Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 4))

    restart_button = pygame.draw.rect(screen, WHITE, (WIDTH // 4, HEIGHT // 2, WIDTH // 5, HEIGHT // 8))
    restart_text = font.render("Restart", True, (0, 0, 0))
    screen.blit(restart_text, (WIDTH // 4 + WIDTH // 16, HEIGHT // 2 + HEIGHT // 32))

    exit_button = pygame.draw.rect(screen, WHITE, (WIDTH // 2, HEIGHT // 2, WIDTH // 6, HEIGHT // 8))
    exit_text = font.render("Exit", True, (0, 0, 0))
    screen.blit(exit_text, (WIDTH // 2 + WIDTH // 16, HEIGHT // 2 + HEIGHT // 32))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if restart_button.collidepoint(event.pos):
                    return True  # Restart
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Main function
def main():
    #  fullscreen mode
    fullscreen = False
    if fullscreen:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
    
    pygame.display.set_caption("Simple Platform Game")
    clock = pygame.time.Clock()

    show_start_screen(screen)

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    weapons = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(3):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    score = 0
    font = pygame.font.Font(None, 36)

    running = True
    paused = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    weapon = Weapon(player.rect)
                    all_sprites.add(weapon)
                    weapons.add(weapon)
                elif event.key == pygame.K_ESCAPE and fullscreen:
                    running = False  # Allow exiting fullscreen mode with the ESC key
                elif event.key == pygame.K_p:  # Press 'P' to pause or resume the game
                    paused = not paused
                elif event.key == pygame.K_q:  # Press 'Q' to quit the game
                    running = False

        if not paused:
            # Check for collisions
            hits = pygame.sprite.groupcollide(weapons, enemies, True, True)
            for hit in hits:
                score += 1
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)

            hits = pygame.sprite.spritecollide(player, enemies, False)
            if hits:
                running = False

            all_sprites.update()

        # Draw
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        if paused:
            pause_text = font.render("Paused", True, WHITE)
            screen.blit(pause_text, (WIDTH // 2 - 50, HEIGHT // 2))

        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    restart = show_end_screen(screen, score)
    if restart:
        main()  # Restart the game

if __name__ == "__main__":
    main()
