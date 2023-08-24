import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
ENEMY_SIZE = 30
BLOCK_SIZE = 50
FPS = 30
ATTACK_DISTANCE = 50
ENEMY_MAX_HEALTH = 3

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adventures in the Wilderness")

# Player starting position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Background map (0: path, 1: tree)
background_map = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

# Enemy variables
enemy_x = 200
enemy_y = 300
enemy_health = ENEMY_MAX_HEALTH

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
        player_x += 5
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - PLAYER_SIZE:
        player_y += 5

    # Draw background
    screen.fill(WHITE)
    for row in range(len(background_map)):
        for col in range(len(background_map[0])):
            if background_map[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            elif background_map[row][col] == 1:
                pygame.draw.rect(screen, BROWN, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # Draw the player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Calculate distance to enemy
    distance_to_enemy = math.sqrt((player_x - enemy_x)**2 + (player_y - enemy_y)**2)

    # Draw the enemy
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE))

    # Attack if close to enemy
    if keys[pygame.K_SPACE] and distance_to_enemy <= ATTACK_DISTANCE:
        enemy_health -= 1
        if enemy_health <= 0:
            enemy_x = -100  # Remove enemy from the game

    # Draw enemy health
    pygame.draw.rect(screen, BLACK, (enemy_x, enemy_y - 10, ENEMY_SIZE, 5))
    pygame.draw.rect(screen, GREEN, (enemy_x, enemy_y - 10, enemy_health * (ENEMY_SIZE / ENEMY_MAX_HEALTH), 5))

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
