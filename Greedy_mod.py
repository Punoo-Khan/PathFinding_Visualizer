from queue import PriorityQueue
import pygame
import sys
from grid import Tile

def heuristic(a, b):
    # Manhattan distance on a grid
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def gbfs(start, end, grid_instance, screen, delay=100):
    queue = PriorityQueue()
    queue.put((0,start))
    visited = set([start])
    parent = {start: None}

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Down, Right, Up, Left

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        distance,current = queue.get()
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
            return path

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            if is_valid(neighbor, grid_instance) and neighbor not in visited:
                dist_neigh = heuristic(neighbor, end)
                visited.add(neighbor)
                parent[neighbor] = current
                queue.put((dist_neigh, neighbor))
                if neighbor != end:
                    grid_instance.tiles[neighbor[1]][neighbor[0]] = Tile.FRONTIER

    return []


def is_valid(pos, grid):
    x, y = pos #the x and y are inverted so x in this case represent col and y is row
    return 0 <= x < len(grid.tiles[0]) and 0 <= y < len(grid.tiles) and (grid.tiles[y][x] == Tile.EMPTY or grid.tiles[y][x] == Tile.END)
    #len(grid.tiles[0]) col in rows and len(grid.tiles) num of rows


def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()
    return path