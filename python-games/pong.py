import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = 5
PADDLE_SPEED = 8

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.radius = 10
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        pygame.draw.circle(window, WHITE, (self.x, self.y), self.radius)

    def collide_with_paddle(self, paddle):
        if self.x - self.radius <= paddle.x + paddle.width and self.y >= paddle.y and self.y <= paddle.y + paddle.height:
            self.dx *= -1

# Paddle class
class Paddle:
    def __init__(self, x):
        self.x = x
        self.y = HEIGHT // 2 - 50
        self.width = 10
        self.height = 100
        self.dy = 0

    def move(self):
        self.y += self.dy
        if self.y < 0:
            self.y = 0
        elif self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

    def draw(self):
        pygame.draw.rect(window, WHITE, (self.x, self.y, self.width, self.height))

# Create objects
ball = Ball()
left_paddle = Paddle(20)
right_paddle = Paddle(WIDTH - 30)

clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                left_paddle.dy = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                left_paddle.dy = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                right_paddle.dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                right_paddle.dy = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                left_paddle.dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                right_paddle.dy = 0

    # Move objects
    ball.move()
    left_paddle.move()
    right_paddle.move()

    # Check collisions
    ball.collide_with_paddle(left_paddle)
    ball.collide_with_paddle(right_paddle)

    # Clear the screen
    window.fill(BLACK)

    # Draw objects
    ball.draw()
    left_paddle.draw()
    right_paddle.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
