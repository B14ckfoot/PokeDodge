# Import the pygame module
from logging import root

import pygame
import random
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set the window icon
icon = pygame.image.load(resource_path("./poke-ball.png"))
pygame.display.set_icon(icon)
pygame.display.set_caption("Poke Dodge")
# Load background music
pygame.mixer.init()
pygame.mixer.music.load('Kingdom Hearts Dearly Beloved (Original Version).mp3')
pygame.mixer.music.play(-1)


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        # Load the player sprite image
        self.original_surf = pygame.image.load(resource_path("./143.png")).convert()
        self.original_surf.set_colorkey((0, 0, 0), RLEACCEL)

        self.scale_factor = 0.8

        self.surf = pygame.transform.scale(self.original_surf, (int(self.original_surf.get_width() * self.scale_factor),
                                                                int(self.original_surf.get_height() * self.scale_factor)))
        self.rect = self.surf.get_rect()
        self.rect.top = 250

    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        global score
        super(Enemy, self).__init__()
        self.original_surf = pygame.image.load(resource_path("./poke-ball.png")).convert()
        self.original_surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.scale_factor = 0.25
        self.surf = pygame.transform.scale(self.original_surf, (int(self.original_surf.get_width() * self.scale_factor),
                                                                int(self.original_surf.get_height() * self.scale_factor)))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        # Use the score to increase difficulty over time
        slow = 3 + score//15
        fast = 7 + score // 10
        self.speed = random.randint(5, 15)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        global score
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            score += 1
#Background Image
image = pygame.image.load(resource_path('./GBA.png'))
def Background_sky(image):
    size = pygame.transform.scale(image, (800, 600))
    screen.blit(size, (0, 0))
# Initialize pygame
pygame.init()

score = 0
SCORE_FONT = pygame.font.Font(None, 36)
# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

# Instantiate player.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
enemies = pygame.sprite.Group()
# - all_sprites is used for rendering everything
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


def draw_score():
    score_surface = SCORE_FONT.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_surface, (10, 10))


# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False
        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)


    # Draw all sprites on top of the background
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    #update player
    player.update(pressed_keys)

    # Update enemy position
    enemies.update()


    # Fill the screen color
    screen.fill((0,255,0))
    Background_sky(image)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    draw_score()

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()

        screen.fill((0, 255, 0))
        Background_sky(image)
         # Display game over message
        game_over_font = pygame.font.Font(None, 48)
        game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)
          # Display final score
        final_score_font = pygame.font.Font(None, 36)
        final_score_text = final_score_font.render(f"Your Score: {score}", True, (0, 0, 0))
        final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(final_score_text, final_score_rect)
            # Display prompt to play again
        play_again_font = pygame.font.Font(None, 36)
        play_again_text = play_again_font.render("Press Y to play again or N to quit", True, (0, 0, 0))
        play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(play_again_text, play_again_rect)


    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(60)