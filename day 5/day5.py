# import pygame
# import random
import pandas
import numpy

# # Initialize Pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption('Breakout')

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)

# # Paddle settings
# PADDLE_WIDTH = 100
# PADDLE_HEIGHT = 10
# PADDLE_SPEED = 10

# # Ball settings
# BALL_SIZE = 10
# BALL_SPEED = 4

# # Brick settings
# BRICK_WIDTH = 75
# BRICK_HEIGHT = 20
# BRICK_ROWS = 4
# BRICK_COLUMNS = 10
# BRICK_PADDING = 5

# def reset_game():
#     global paddle, ball, ball_dx, ball_dy, bricks, game_over
#     # Initialize paddle
#     paddle = pygame.Rect((SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30), (PADDLE_WIDTH, PADDLE_HEIGHT))

#     # Initialize ball
#     ball = pygame.Rect((SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2), (BALL_SIZE, BALL_SIZE))
#     ball_dx = BALL_SPEED * random.choice([-1, 1])
#     ball_dy = -BALL_SPEED

#     # Initialize bricks
#     bricks = []
#     for row in range(BRICK_ROWS):
#         for col in range(BRICK_COLUMNS):
#             brick = pygame.Rect(
#                 col * (BRICK_WIDTH + BRICK_PADDING) + BRICK_PADDING,
#                 row * (BRICK_HEIGHT + BRICK_PADDING) + BRICK_PADDING,
#                 BRICK_WIDTH,
#                 BRICK_HEIGHT
#             )
#             bricks.append(brick)
    
#     game_over = False

# reset_game()

# # Main game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
#             mouse_pos = event.pos
#             if restart_button.collidepoint(mouse_pos):
#                 reset_game()
#             if quit_button.collidepoint(mouse_pos):
#                 running = False

#     # Handle paddle movement
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and paddle.left > 0:
#         paddle.move_ip(-PADDLE_SPEED, 0)
#     if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
#         paddle.move_ip(PADDLE_SPEED, 0)

#     # paddle.centerx = ball.centerx

#     if not game_over:
#         # Move ball
#         ball.x += ball_dx
#         ball.y += ball_dy

#         # Ball collision with walls
#         if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
#             ball_dx = -ball_dx
#         if ball.top <= 0:
#             ball_dy = -ball_dy
#         if ball.bottom >= SCREEN_HEIGHT:
#             game_over = True

#         # Ball collision with paddle
#         if ball.colliderect(paddle):
#             ball_dy = -ball_dy

#         # Ball collision with bricks
#         for brick in bricks[:]:
#             if ball.colliderect(brick):
#                 bricks.remove(brick)
#                 ball_dy = -ball_dy
#                 break

#     # Clear screen
#     screen.fill(BLACK)

#     # Draw paddle
#     pygame.draw.rect(screen, BLUE, paddle)

#     # Draw ball
#     pygame.draw.ellipse(screen, WHITE, ball)
#     font = pygame.font.Font(None, 24)
#     text = font.render(f"x: {ball.x}, y: {ball.y}", True, WHITE)
#     text_rect = text.get_rect()
#     text_rect.topleft = (ball.right + 10, ball.top)
#     screen.blit(text, text_rect)

#     # Draw bricks
#     for brick in bricks:
#         pygame.draw.rect(screen, RED, brick)

#     if game_over:
#         # Draw "Game Over" message
#         font = pygame.font.Font(None, 74)
#         text = font.render("Game Over", True, WHITE)
#         screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))

#         # Draw restart button
#         restart_button = pygame.Rect(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 50, 100, 50)
#         pygame.draw.rect(screen, GREEN, restart_button)
#         font = pygame.font.Font(None, 36)
#         text = font.render("Restart", True, BLACK)
#         text_rect = text.get_rect(center=restart_button.center)
#         screen.blit(text, text_rect.topleft)

#         quit_button = pygame.Rect(SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2 + 125, 100, 50)
#         pygame.draw.rect(screen, GREEN, quit_button)
#         font = pygame.font.Font(None, 36)
#         text = font.render("Quit", True, BLACK)
#         text_rect = text.get_rect(center=quit_button.center)
#         screen.blit(text, text_rect.topleft)

#     # Update display
#     pygame.display.flip()

#     # Cap the frame rate
#     pygame.time.Clock().tick(60)

# # Quit Pygame
# pygame.quit()


def move_A(n):
    print(f"{' ' * n}")
    for position in range (0,n):
        white1 = " " * (position)
        white2 = " " * (n - position - 1)
        print(f"{white1}A{white2}")
    print(f"{' ' * n}")
# move_A(5)

def move_AA(n):
    print(f"{'_' * (n - 1)}")
    for position in range (0,n):
        white1 = "_" * (position - 1)
        white2 = "_" * (n - position - 2)
        if position == 0 or position == (n - 1):
            x = "A"
        else:
            x = "AA"
        print(f"{white1}{x}{white2}")
    print(f"{'_' * (n - 1)}")
# move_AA(5)

def move_NAs(a):
    n = a + 6
    for position in range (0,n):
        white1 = "_" * (position - a)
        white2 = "_" * (n - position - a)
        if position <= (a):
            x = "A" * (position)
        elif position >= a and position < (n - a):
            x = "A" * a
        else:
            x = "A" * (n - position)
        print(f"{white1}{x}{white2}")
    print(f"{'_' * (n - a)}")
move_NAs(5)



