from collections import deque
import pygame
import random
import sys
from grid import Grid, Tile  # Import the Grid class and the Tile enum
from BFS_mod import bfs  # Import the bfs function
from Greedy_mod import gbfs
from A_star import Astar
from enum import Enum, auto
import Button
import copy
import time

start_set = False
end_set = False
WINDOW_SIZE = (800, 600)
GRID_SIZE = (20, 15) #dimesions of grid
bfs_button = Button.button(650, 550, 100, 40, 'START')
random_button = Button.button(400, 550, 100, 40, 'RANDOM')

def generate_random_map(grid):
    global start_set
    global end_set
    # Clear the grid first to reset any previous configurations
    grid.clear_grid()

    # Randomly choose start and end positions
    start_x = random.randint(0, grid.size[0] - 1)
    start_y = random.randint(0, grid.size[1] - 1)
    end_x, end_y = start_x, start_y

    # Ensure end is not the same as start
    while (end_x, end_y) == (start_x, start_y):
        end_x = random.randint(0, grid.size[0] - 1)
        end_y = random.randint(0, grid.size[1] - 1)

    grid.start_pos = (start_x, start_y)
    grid.end_pos = (end_x, end_y)
    grid.set_start(grid.start_pos)
    grid.set_end(grid.end_pos)
    start_set = True
    end_set = True

    # Randomly place walls, avoiding start and end positions
    for y in range(grid.size[1]):
        for x in range(grid.size[0]):
            if (x, y) == grid.start_pos or (x, y) == grid.end_pos:
                continue
            grid.tiles[y][x] = Tile.WALL if random.random() < 0.3 else Tile.EMPTY

def main():
    global start_set
    global end_set
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

                        start_time = time.time()
                        # Ensure grid state is reset before GBFS
                        grid.tiles = copy.deepcopy(saved_tiles)
                        grid.draw()
                        pygame.display.flip()
                        print(gbfs(grid.start_pos, grid.end_pos, grid, screen))
                        end_time = time.time()
                        time_taken = end_time - start_time
                        print(f"GREEDY BFS Algorithm took {time_taken:.2f} seconds to complete.")

                        start_time = time.time()
                        # # Ensure grid state is reset before A*
                        grid.tiles = copy.deepcopy(saved_tiles)
                        grid.draw()
                        pygame.display.flip()
                        print(Astar(grid.start_pos, grid.end_pos, grid, screen))
                        end_time = time.time()
                        time_taken = end_time - start_time
                        print(f"A* Algorithm took {time_taken:.2f} seconds to complete.")
                    else:
                        pass
                elif random_button.is_clicked(mouse_pos):
                    generate_random_map(grid)
                    grid.draw()
                    pygame.display.flip()
                # Left click for walls, start, and end
                elif event.button == 1:
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
        random_button.draw(screen)
        pygame.display.flip()

        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()