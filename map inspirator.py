import pygame
import random

# Initialize pygame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
MAP_WIDTH, MAP_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
PLAYER_SPEED = 10  # Adjust player speed (higher value = slower movement)
MOVE_DELAY = 10   # Frames to wait before moving player

# Create a new map
def generate_map(density):
    return [[1 if random.random() < density else 0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

# Initialize player position
player_x, player_y = random.choice([0, MAP_WIDTH - 1]), random.randint(0, MAP_HEIGHT - 1)
move_counter = 0

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Map Generator")

# Main loop
running = True
density = 0.4  # Initial map density
current_map = generate_map(density)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_UP]:
        dy -= 1
    if keys[pygame.K_DOWN]:
        dy += 1
    if keys[pygame.K_LEFT]:
        dx -= 1
    if keys[pygame.K_RIGHT]:
        dx += 1

    move_counter += 1
    if move_counter >= MOVE_DELAY:
        # Check if the new position is valid (not a black block)
        new_x = player_x + dx
        new_y = player_y + dy

        if 0 <= new_x < MAP_WIDTH and 0 <= new_y < MAP_HEIGHT and current_map[new_y][new_x] == 0:
            player_x = new_x
            player_y = new_y

        move_counter = 0

    # Check if player is walking off screen and regen map
    if (player_x == 0 and dx == -1) or (player_x == MAP_WIDTH - 1 and dx == 1) or \
       (player_y == 0 and dy == -1) or (player_y == MAP_HEIGHT - 1 and dy == 1):
        current_map = generate_map(density)
        player_x, player_y = MAP_WIDTH // 2, MAP_HEIGHT // 2

    # Draw the map
    screen.fill((255, 255, 255))  # Set background to white
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if current_map[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, (255, 0, 0), (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit the frame rate

# Clean up
pygame.quit()
