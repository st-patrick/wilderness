import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_SIZE = 600  # Screen will be square
PLAYER_SIZE = 40
ENEMY_SIZE = 40  # Increase enemy size for easier hit detection
FPS = 30
ATTACK_DISTANCE = 100  # Increase attack distance
ENEMY_MAX_HEALTH = 10  # Increase enemy health

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLACK = (0, 0, 0)

# Create the screen (square)
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Adventures in the Wilderness")

# Player starting position
player_x = SCREEN_SIZE // 2
player_y = SCREEN_SIZE // 2

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

# Calculate block size based on screen size and map length
block_size = SCREEN_SIZE // len(background_map)

# Calculate player collision size
player_collision_size = PLAYER_SIZE // 2

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    new_player_x = player_x
    new_player_y = player_y
    if keys[pygame.K_LEFT] and player_x - player_collision_size > 0:
        new_player_x -= 5
    if keys[pygame.K_RIGHT] and player_x + player_collision_size < SCREEN_SIZE:
        new_player_x += 5
    if keys[pygame.K_UP] and player_y - player_collision_size > 0:
        new_player_y -= 5
    if keys[pygame.K_DOWN] and player_y + player_collision_size < SCREEN_SIZE:
        new_player_y += 5

    # Check if new player position is valid
    player_top_left = (new_player_x - player_collision_size, new_player_y - player_collision_size)
    player_top_right = (new_player_x + player_collision_size, new_player_y - player_collision_size)
    player_bottom_left = (new_player_x - player_collision_size, new_player_y + player_collision_size)
    player_bottom_right = (new_player_x + player_collision_size, new_player_y + player_collision_size)

    invalid_move = False
    for point in [player_top_left, player_top_right, player_bottom_left, player_bottom_right]:
        row = point[1] // block_size
        col = point[0] // block_size
        if background_map[row][col] == 1:
            invalid_move = True
            break

    if not invalid_move:
        player_x = new_player_x
        player_y = new_player_y

    # Draw background
    screen.fill(WHITE)
    for row in range(len(background_map)):
        for col in range(len(background_map[0])):
            if background_map[row][col] == 0:
                pygame.draw.rect(screen, WHITE, (col * block_size, row * block_size, block_size, block_size))
            elif background_map[row][col] == 1:
                pygame.draw.rect(screen, BROWN, (col * block_size, row * block_size, block_size, block_size))

    # Draw the player
    pygame.draw.rect(screen, GREEN, (player_x - player_collision_size, player_y - player_collision_size, PLAYER_SIZE, PLAYER_SIZE))

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
