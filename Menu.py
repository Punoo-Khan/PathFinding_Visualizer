import pygame
import sys

# Initialize Pygame
pygame.init()
# Load the image

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Text Buttons")


background_image = pygame.image.load('Background.jpg')
bg_width, bg_height = background_image.get_size()

# Create a surface to hold the tiled image
bg_surface = pygame.Surface((bg_width * 2, bg_height * 2))
for x in range(0, bg_width * 2, bg_width):
    for y in range(0, bg_height * 2, bg_height):
        bg_surface.blit(background_image, (x, y))

# The offset for the illusion of moving "into" the screen
offset_x, offset_y = 0, 0


# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255,0,0)
CYAN = (0, 240, 255)
# Define the Button class
class Button:
    def __init__(self, text, font, x, y, color):
        self.text = text
        self.font = font
        self.color = color
        self.image = font.render(text, True, self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, event_type):
        return self.rect.collidepoint(mouse_pos) and event_type == pygame.MOUSEBUTTONDOWN

# Create a font object
font = pygame.font.SysFont('Jokerman', 20)

# Create text buttons
button1 = Button("Create Your Own Map ", font, 300, 300, WHITE)
button2 = Button("Create a Random Map", font, 300, 350, WHITE)

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            if button1.is_hovered(mouse_pos):
                button1.image = font.render(button1.text, True, GREEN)
            else:
                button1.image = font.render(button1.text, True, CYAN)
            if button2.is_hovered(mouse_pos):
                button2.image = font.render(button2.text, True, GREEN)
            else:
                button2.image = font.render(button2.text, True, CYAN)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button1.is_clicked(mouse_pos, event.type):
                # Perform actions when button 1 is clicked
                print("Button 1 clicked!")
                button1.image = font.render(button1.text, True, RED)  # Change color to red when clicked
            elif button2.is_clicked(mouse_pos, event.type):
                # Perform actions when button 2 is clicked
                print("Button 2 clicked!")
                button2.image = font.render(button2.text, True, RED)  # Change color to red when clicked

     # Update the offset
    offset_x += 2
    offset_y += 2
    if offset_x > bg_width: offset_x = 0
    if offset_y > bg_height: offset_y = 0

    # Draw the background image with the updated offset
    for x in range(-offset_x, WINDOW_WIDTH, bg_width):
        for y in range(-offset_y, WINDOW_HEIGHT, bg_height):
            window.blit(background_image, (x, y))
    # Draw buttons
    button1.draw(window)
    button2.draw(window)
    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
