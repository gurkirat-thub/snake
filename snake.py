import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
BLOCK_SIZE = 20
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake')

# Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

# FPS (frames per second) controller
fps_controller = pygame.time.Clock()

def random_snack_position():
    x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return [x, y]

def main():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]

    direction = 'RIGHT'
    change_to = direction

    snack_pos = random_snack_position()
    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RIGHT, pygame.K_d) and direction != 'LEFT':
                    change_to = 'RIGHT'
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key in (pygame.K_UP, pygame.K_w) and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != 'UP':
                    change_to = 'DOWN'

        direction = change_to

        if direction == 'RIGHT':
            snake_pos[0] += BLOCK_SIZE
        elif direction == 'LEFT':
            snake_pos[0] -= BLOCK_SIZE
        elif direction == 'UP':
            snake_pos[1] -= BLOCK_SIZE
        elif direction == 'DOWN':
            snake_pos[1] += BLOCK_SIZE

        # Snake body growing mechanism
        snake_body.insert(0, list(snake_pos))
        if snake_pos == snack_pos:
            score += 1
            snack_pos = random_snack_position()
            # Make sure snack does not spawn on the snake
            while snack_pos in snake_body:
                snack_pos = random_snack_position()
        else:
            snake_body.pop()

        # Game over conditions
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            break

        # Snake collision with itself
        if snake_pos in snake_body[1:]:
            break

        # Draw
        screen.fill(BLACK)
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(snack_pos[0], snack_pos[1], BLOCK_SIZE, BLOCK_SIZE))

        # Score
        font = pygame.font.SysFont('arial', 24)
        score_surface = font.render('Score: ' + str(score), True, WHITE)
        screen.blit(score_surface, (10, 10))

        pygame.display.flip()
        fps_controller.tick(10)

    # Game over display
    font = pygame.font.SysFont('arial', 48)
    game_over_surface = font.render('Game Over', True, RED)
    game_over_rect = game_over_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
