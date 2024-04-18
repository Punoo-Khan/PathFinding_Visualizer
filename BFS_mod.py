from collections import deque
import pygame
import sys
from grid import Tile
from Audio import SoundManager

tiles_visited = 0
path_length = 1 # intialzing at 1 because it isnt counting end at the function
def bfs(start, end, grid_instance, screen, delay=100):
    global tiles_visited
    global path_length
    queue = deque([start])
    visited = set([start])
    parent = {start: None}
    sound = SoundManager()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left
    total_distance = calc_distance(start,end)
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        current = queue.popleft()
        current_distance = calc_distance(current, end)
        if current_distance > 0.0 and total_distance > 0.0:
            ratio = total_distance/current_distance
            #ratio = 1 - ratio
            #print(ratio)
            #sound.play_sound(volume=1.0,pitch=ratio)
        if current != start:
            grid_instance.tiles[current[1]][current[0]] = Tile.VISITED
            grid_instance.draw()
            #bfs_button.draw(screen)
            pygame.display.flip()
            pygame.time.delay(delay)  # Delay for visualization

        if current == end:
            path = reconstruct_path(parent, start, end)
            for pos in path:
                grid_instance.tiles[pos[1]][pos[0]] = Tile.PATH
                grid_instance.draw()
                pygame.display.flip()
                pygame.time.delay(delay)
            print(f"the path length is {path_length} and the tiles visited by BFS is {tiles_visited}")
            return path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor, grid_instance) and neighbor not in visited:
                visited.add(neighbor)
                tiles_visited += 1
                parent[neighbor] = current
                queue.append(neighbor)
                if neighbor != end:
                    grid_instance.tiles[neighbor[1]][neighbor[0]] = Tile.FRONTIER
    return []


def is_valid(pos, grid):
    x, y = pos #the x and y are inverted so x in this case represent col and y is row
    return 0 <= x < len(grid.tiles[0]) and 0 <= y < len(grid.tiles) and (grid.tiles[y][x] == Tile.EMPTY or grid.tiles[y][x] == Tile.END)
    #len(grid.tiles[0]) col in rows and len(grid.tiles) num of rows


def reconstruct_path(parent, start, end):
    global path_length
    path = []
    current = end
    while current != start:
        path_length += 1
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path

def calc_distance(start,end):
    (x1, y1) = start
    (x2, y2) = end
    return abs(x1 - x2) + abs(y1 - y2)