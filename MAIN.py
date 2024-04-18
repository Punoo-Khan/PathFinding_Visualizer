from collections import deque
import pygame
import sys
from grid import Grid, Tile  # Import the Grid class and the Tile enum
from BFS_mod import bfs  # Import the bfs function
from Greedy_mod import gbfs
from A_star import Astar
from enum import Enum, auto
import Button
import copy
import time

WINDOW_SIZE = (800, 600)
GRID_SIZE = (20, 15) #dimesions of grid
bfs_button = Button.button(650, 550, 100, 40, 'Nigga BFS')
def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    clock = pygame.time.Clock()
    grid = Grid(screen, GRID_SIZE, WINDOW_SIZE)

    start_set = False
    end_set = False
    saved_tiles = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                tile_pos = grid.get_tile_pos(mouse_pos)

                if bfs_button.is_clicked(mouse_pos):
                    if start_set and end_set:
                        saved_tiles = copy.deepcopy(grid.tiles)
                        start_time = time.time()
                        # Run BFS
                        print(bfs(grid.start_pos, grid.end_pos, grid, screen))
                        end_time = time.time()
                        time_taken = end_time - start_time
                        print(f"BFS Algorithm took {time_taken:.2f} seconds to complete.")

                        # # Ensure grid state is reset before GBFS
                        # grid.tiles = copy.deepcopy(saved_tiles)
                        # grid.draw()
                        # pygame.display.flip()
                        # print(gbfs(grid.start_pos, grid.end_pos, grid, screen))
                        #
                        # # Ensure grid state is reset before A*
                        # grid.tiles = copy.deepcopy(saved_tiles)
                        # grid.draw()
                        # pygame.display.flip()
                        # print(Astar(grid.start_pos, grid.end_pos, grid, screen))
                # Left click for walls, start, and end
                if event.button == 1:
                    #print(start_set, tile_pos)
                    if not start_set:
                        grid.set_start(tile_pos)
                        start_set = True
                    elif not end_set:
                        grid.set_end(tile_pos)
                        end_set = True
                    else:
                        grid.toggle_wall(tile_pos)

                # Right click to reset a cell
                elif event.button == 3:
                   # print(start_set, tile_pos, "nigga",grid.start_pos )
                    grid.set_tile(tile_pos, Tile.EMPTY)
                    if start_set and tile_pos == grid.start_pos:
                        start_set = False
                    if end_set and tile_pos == grid.end_pos:
                        end_set = False

        screen.fill((60, 70, 90))  # Clear screen with a different background color

        grid.draw()  # Draw the grid
        bfs_button.draw(screen)  # Draw the BFS button
        pygame.display.flip()

        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()