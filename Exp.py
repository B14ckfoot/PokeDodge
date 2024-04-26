import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RPG Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define fonts
font = pygame.font.Font(None, 36)

class Character:
    def __init__(self, name, hp, attack, defense, max_hp):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.max_hp = max_hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def attack_target(self, target):
        damage = max(0, self.attack - target.defense)
        target.take_damage(damage)
        return damage

class Enemy(Character):
    def __init__(self, name, hp, attack, defense, max_hp):
        super().__init__(name, hp, attack, defense, max_hp)

# Function to display text on screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw health bars
def draw_health_bar(character, x, y):
    bar_length = 100
    bar_height = 10
    fill = (character.hp / character.max_hp) * bar_length
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(screen, GREEN, fill_rect)
    pygame.draw.rect(screen, WHITE, outline_rect, 2)

def main():
    player = Character("Player", hp=50, attack=8, defense=5, max_hp=50)
    enemies = [
        Enemy("Goblin", hp=30, attack=6, defense=2, max_hp=30),
        Enemy("Orc", hp=50, attack=10, defense=4, max_hp=50),
        Enemy("Dragon", hp=100, attack=15, defense=10, max_hp=100)
    ]

    running = True
    current_enemy = None
    battle_active = False

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not battle_active:
                        battle_active = True
                        current_enemy = random.choice(enemies)

        if battle_active:
            draw_text("Battle!", font, WHITE, SCREEN_WIDTH // 2, 50)
            draw_text("Press SPACE to attack", font, WHITE, SCREEN_WIDTH // 2, 100)

            draw_text(f"Player HP: {player.hp}/{player.max_hp}", font, WHITE, 100, 200)
            draw_text(f"Enemy HP: {current_enemy.hp}/{current_enemy.max_hp}", font, WHITE, SCREEN_WIDTH - 100, 200)

            draw_health_bar(player, 100, 250)
            draw_health_bar(current_enemy, SCREEN_WIDTH - 200, 250)

            if player.is_alive() and current_enemy.is_alive():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_damage = player.attack_target(current_enemy) 
                        enemy_damage = current_enemy.attack_target(player)
                        draw_text(f"Player attacks for {player_damage} damage", font, RED, SCREEN_WIDTH // 2, 300)
                        draw_text(f"Enemy attacks for {enemy_damage} damage", font, RED, SCREEN_WIDTH // 2, 350)

                if not player.is_alive():
                    draw_text("You were defeated! Game Over!", font, RED, SCREEN_WIDTH // 2, 400)
                    battle_active = False
                elif not current_enemy.is_alive():
                    draw_text("You defeated the enemy!", font, GREEN, SCREEN_WIDTH // 2, 400)
                    battle_active = False
            else:
                if not player.is_alive():
                    draw_text("You were defeated! Game Over!", font, RED, SCREEN_WIDTH // 2, 400)
                elif not current_enemy.is_alive():
                    draw_text("You defeated the enemy!", font, GREEN, SCREEN_WIDTH // 2, 400)
                battle_active = False
        else:
            draw_text("Press SPACE to start a battle", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
