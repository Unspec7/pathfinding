from collections import defaultdict
from itertools import product
import random
from PIL import Image

# List of cardinal directions.
_DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def generate_graph(size):
    """

    Return size-by-size maze graph in the form of a mapping from vertex
    coordinates to sets of coordinates of neighbouring vertices, that is:

        graph[x, y] = {(x1, y1), (x2, y2), ...}

    Vertices are placed at odd coordinates, leaving room for walls.

    """
    graph = defaultdict(set)
    coords = range(1, size * 2, 2)
    for x, y in product(coords, repeat=2):
        for dx, dy in _DIRECTIONS:
            nx, ny = x + dx * 2, y + dy * 2
            if nx in coords and ny in coords:
                graph[x, y].add((nx, ny))
    return graph


def generate_maze(graph):
    """

    Given a graph as returned by generate_graph, return the set of
    coordinates on the path in a random maze on that graph.

    """
    v = random.choice(list(graph)) # Current vertex.
    stack = [v]                    # Depth-first search stack.
    path = set()        # Visited vertices and the walls between them.
    while stack:
        path.add(v)
        neighbours = graph[v] - path
        if neighbours:
            x, y = v
            nx, ny = neighbour = random.choice(list(neighbours))
            wall = (x + nx) // 2, (y + ny) // 2
            path.add(wall)
            stack.append(neighbour)
            v = neighbour
        else:
            v = stack.pop()
    return path


def generate_image(filename, size, path):
    """

    Create a size-by-size black-and-white image, with white on path and
    black elsewhere, and save it to filename.

    """
    image = Image.new('1', (size, size))
    pixels = image.load()
    for p in path:
        pixels[p] = 1
    image.save(filename)


def create(filename, size):

    """"

    Create a size-by-size maze and save it to filename.

    """

    ext = '.png'
    if not filename.endswith(ext):
        filename += ext
    size_real = (2 * size) + 1
    graph = generate_graph(size)
    path = generate_maze(graph)

    # Ensure the squares the target and agent are on are clear
    path.update([(1, 0), (size_real - 1, size_real - 2)])
    generate_image(filename, size_real, path)


for x in range(1, 51):
    print ("Generating maze number", x)
    create("maze" + str(x), 101)
