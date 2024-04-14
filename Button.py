import pygame

class button:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = (200, 200, 200)  # Light gray

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.text != '':
            font = pygame.font.SysFont('Jokerman', 20)
            text = font.render(self.text, True, (0, 0, 0))  # Black text
            screen.blit(text, (self.rect.x + (self.rect.width - text.get_width()) // 2,
                               self.rect.y + (self.rect.height - text.get_height()) // 2)
                        )

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

