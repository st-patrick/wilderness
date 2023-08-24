import pygame
import random

pygame.init()

# Constants
SCREEN_SIZE = 800
MAP_SIZE = 10
BLOCK_SIZE = SCREEN_SIZE // MAP_SIZE
BLOCK_PROBABILITY = 0.3

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Generate initial map
def generate_map(size):
    return [[1 if random.random() < BLOCK_PROBABILITY else 0 for _ in range(size)] for _ in range(size)]

# Draw the map
def draw_map(screen, game_map):
    for y in range(MAP_SIZE):
        for x in range(MAP_SIZE):
            color = WHITE if game_map[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Main function
def main():
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Random Map Generator")

    clock = pygame.time.Clock()

    current_map = generate_map(MAP_SIZE)
    player_x, player_y = MAP_SIZE // 2, MAP_SIZE // 2

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_y -= 1
        if keys[pygame.K_s]:
            player_y += 1
        if keys[pygame.K_a]:
            player_x -= 1
        if keys[pygame.K_d]:
            player_x += 1

        if player_x < 0 or player_x >= MAP_SIZE or player_y < 0 or player_y >= MAP_SIZE:
            current_map = generate_map(MAP_SIZE)
            player_x, player_y = MAP_SIZE // 2, MAP_SIZE // 2

        screen.fill(WHITE)
        draw_map(screen, current_map)
        pygame.draw.rect(screen, (255, 0, 0), (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
