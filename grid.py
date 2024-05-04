
import pygame
from enum import Enum, auto
import Button


# Enum to represent tile types
class Tile(Enum):
    EMPTY = auto()
    WALL = auto()
    START = auto()
    END = auto()
    VISITED = auto()
    FRONTIER = auto()
    PATH = auto()



# Define colors
COLORS = {
    Tile.EMPTY: (255, 255, 255),  # White
    Tile.WALL: (0, 0, 0),         # Black
    Tile.START: (50, 235, 50),    # Green
    Tile.END: (235, 50, 50),      # Red
    Tile.VISITED: (196, 195, 195 ),# Gray
    Tile.FRONTIER: (64, 224, 208), # Cyan
    Tile.PATH: (128, 128, 255)  # Example path color
}


# Configuration for the window


class Grid:
    def __init__(self, screen, size, WINDOW_SIZE):
        self.screen = screen
        self.size = size
        self.tiles = [[Tile.EMPTY for _ in range(size[0])] for _ in range(size[1])] #2d list of tiles
        self.tile_size = (WINDOW_SIZE[0] // size[0], WINDOW_SIZE[1] // size[1])
        self.start_pos = auto()
        self.end_pos = auto()

    def draw(self):
        #current index x and list of the current row which will contain the coloumn in that row
        for x, row in enumerate(self.tiles):
            #current index y and the current tile/coloumn in that row
            for y, tile in enumerate(row):
                rect = pygame.Rect(y*self.tile_size[0], x*self.tile_size[1], *self.tile_size) # since 0 is col i have multi it to y and 1 to 0 and lastly last arg is use to unpack tuple
                pygame.draw.rect(self.screen, COLORS[tile], rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # Draw border of the tile nigga

    def get_tile_pos(self, mouse_pos):
        return mouse_pos[0] // self.tile_size[0], mouse_pos[1] // self.tile_size[1]

    def clear_grid(self):
        self.tiles = [[Tile.EMPTY for _ in range(self.size[0])] for _ in range(self.size[1])]


    def set_start(self, pos):
        self.tiles[pos[1]][pos[0]] = Tile.START
        self.start_pos =(pos[0],pos[1])

    def set_end(self, pos):
        self.tiles[pos[1]][pos[0]] = Tile.END
        self.end_pos = (pos[0],pos[1])

    def toggle_wall(self, pos):
        if self.tiles[pos[1]][pos[0]] == Tile.WALL:
            self.tiles[pos[1]][pos[0]] = Tile.EMPTY
        elif self.tiles[pos[1]][pos[0]] == Tile.START or self.tiles[pos[1]][pos[0]] == Tile.END:
            pass
        else:
            self.tiles[pos[1]][pos[0]] = Tile.WALL

    def set_tile(self, pos, tile_type):
        self.tiles[pos[1]][pos[0]] = tile_type

