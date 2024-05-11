import pygame

class button:
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


