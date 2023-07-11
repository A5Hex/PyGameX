import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Example")

# Set up the initial position of the square
x, y = width // 2, height // 2

# Set up the size of the square
size = 50

# Set up the colors
red = pygame.Color(255, 0, 0)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keyboard inputs
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the square
    pygame.draw.rect(screen, red, pygame.Rect(x, y, size, size))

    # Update the display
    pygame.display.flip()
