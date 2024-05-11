import pygame
from enum import Enum, auto

class Tile(Enum):
    EMPTY = auto()
    WALL = auto()
    START = auto()
    END = auto()
    VISITED = auto()
    FRONTIER = auto()
    PATH = auto()
    GREEN = auto()
    RED = auto()

COLORS = {
    Tile.WALL: (243, 243, 243),   # White
    Tile.EMPTY: (0, 0, 0),        # Black
    Tile.VISITED: (196, 195, 195),# Gray
    Tile.FRONTIER: (48, 171, 178),# Cyan
    Tile.PATH: (128, 128, 255),   # Example path color
    Tile.GREEN: (0, 255, 0),
    Tile.RED: (255, 0, 0)
}

class Grid:
    def __init__(self, screen, size, WINDOW_SIZE):
        self.screen = screen
        self.size = size
        self.tiles = [[Tile.EMPTY for _ in range(size[0])] for _ in range(size[1])]
        self.tile_size = (WINDOW_SIZE[0] // size[0], WINDOW_SIZE[1] // size[1])
        self.start_pos = auto()
        self.end_pos = auto()
        self.start_image = pygame.transform.scale(pygame.image.load('xd.png'), self.tile_size)
        self.end_image = pygame.transform.scale(pygame.image.load('nigga2.jpeg'), self.tile_size)
        self.wall_image = pygame.transform.scale(pygame.image.load('nigga.jpeg'), self.tile_size)

    def draw(self):
        for x, row in enumerate(self.tiles):
            for y, tile in enumerate(row):
                rect = pygame.Rect(y * self.tile_size[0], x * self.tile_size[1], *self.tile_size)
                if tile == Tile.START:
                    self.screen.blit(self.start_image, rect.topleft)
                elif tile == Tile.END:
                    self.screen.blit(self.end_image, rect.topleft)
                elif tile == Tile.WALL:
                    self.screen.blit(self.wall_image, rect.topleft)
                else:
                    pygame.draw.rect(self.screen, COLORS[tile], rect)
                    pygame.draw.rect(self.screen, COLORS[Tile.WALL], rect, 1)

    def get_tile_pos(self, mouse_pos):
        return mouse_pos[0] // self.tile_size[0], mouse_pos[1] // self.tile_size[1]

    def clear_grid(self):
        self.tiles = [[Tile.EMPTY for _ in range(self.size[0])] for _ in range(self.size[1])]

    def set_start(self, pos):
        self.tiles[pos[1]][pos[0]] = Tile.START
        self.start_pos = (pos[0], pos[1])

    def set_end(self, pos):
        self.tiles[pos[1]][pos[0]] = Tile.END
        self.end_pos = (pos[0], pos[1])

    def toggle_wall(self, pos):
        if self.tiles[pos[1]][pos[0]] == Tile.WALL:
            self.tiles[pos[1]][pos[0]] = Tile.EMPTY
        elif self.tiles[pos[1]][pos[0]] == Tile.START or self.tiles[pos[1]][pos[0]] == Tile.END:
            pass
        else:
            self.tiles[pos[1]][pos[0]] = Tile.WALL

    def set_tile(self, pos, tile_type):
        self.tiles[pos[1]][pos[0]] = tile_type

