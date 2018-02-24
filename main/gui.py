import pygame
from generators import MazeGenDF
from astar import AStarSolver
from maze import SquareMaze as Maze



class PyMaze:
    FPS = 50
    COLOR_BG = (255, 255, 255)
    COLOR_TILE = (110, 110, 110)
    COLOR_ACTIVE = (255, 155, 0)
    COLOR_STARTEND = (0, 180, 255)
    COLOR_PATH = (200, 230, 230)
    WALL_SIZE = 3
    OFFSET = 10

    def __init__(self, screen_size=820, name="PyMaze", generate_speed=1,
                 solve_speed=1, size=80):
        self.screen_size = screen_size
        self.name = name
        self.maze = Maze(size)
        self.maze_size, self.tile_size = self.set_dimensions()
        self.gen = MazeGenDF(self.maze)
        self.generate_speed = generate_speed
        self.solve_speed = solve_speed
        self.solver = AStarSolver(self.maze)

    def set_dimensions(self):
        maze_size = self.screen_size - 2*self.OFFSET
        tile_size = (maze_size / self.maze.grid_size)
        return maze_size, tile_size

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_size,
                                          self.screen_size))
        pygame.display.set_caption(self.name)

        clock = pygame.time.Clock()
        running = True
        make_maze = False
        solve_maze = False
        current = None

        while running:
            if current:
                current.tile.active = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    make_maze = not make_maze
                    if self.maze.finished():
                        solve_maze = not solve_maze
                if event.type == pygame.QUIT:
                    running = False

            if make_maze and not self.maze.finished():
                for _ in xrange(self.generate_speed):
                    self.gen.step()

            if solve_maze and not self.solver.done:
                for _ in xrange(self.solve_speed):
                    current = self.solver.step(current)
                if current:
                    current.tile.active = True
                if self.solver.done:
                    for node in self.solver.path:
                        node.tile.in_path = True
                    for wall in self.solver.path_walls:
                        wall.in_path = True

            screen.fill(self.COLOR_BG)
            self.draw_maze(screen)
            pygame.display.flip()
            clock.tick(self.FPS)

        pygame.quit()

    def draw_maze(self, screen):
        self.draw_walls(screen)
        self.draw_tiles(screen)

    def draw_walls(self, screen):
        x = self.OFFSET
        y = self.OFFSET

        for j in xrange(self.maze.grid_size + 1):
            for i in xrange(self.maze.grid_size + 1):
                # Draw dot
                pygame.draw.rect(screen, self.COLOR_TILE, (x, y,
                                                           self.WALL_SIZE,
                                                           self.WALL_SIZE))

                wall_length = self.tile_size - self.WALL_SIZE

                # Draw horizontal walls
                if i < self.maze.grid_size:
                    hor = self.maze.walls[(i, j, 'h')]
                    if hor.startend:
                        color = self.COLOR_STARTEND
                    elif hor.in_path:
                        color = self.COLOR_PATH
                    else:
                        color = self.COLOR_TILE if hor.filled else self.COLOR_BG
                    pygame.draw.rect(screen, color,
                                     (x + self.WALL_SIZE, y,
                                      wall_length, self.WALL_SIZE))

                # Draw vertical walls
                if j < self.maze.grid_size:
                    pass
                    ver = self.maze.walls[(i, j, 'v')]
                    if ver.startend:
                        color = self.COLOR_STARTEND
                    elif ver.in_path:
                        color = self.COLOR_PATH
                    else:
                        color = self.COLOR_TILE if ver.filled else self.COLOR_BG
                    pygame.draw.rect(screen, color,
                                     (x, y + self.WALL_SIZE,
                                      self.WALL_SIZE, wall_length))

                x += self.tile_size

            x = self.OFFSET
            y += self.tile_size

    def draw_tiles(self, screen):
        x = self.OFFSET + self.WALL_SIZE
        y = self.OFFSET + self.WALL_SIZE
        rect_size = self.tile_size - self.WALL_SIZE

        for j in xrange(self.maze.grid_size):
            for i in xrange(self.maze.grid_size):
                tile = self.maze.tiles[(i, j)]

                if tile.active:
                    color = self.COLOR_ACTIVE
                elif tile.startend:
                    color = self.COLOR_STARTEND
                elif tile.in_path:
                    color = self.COLOR_PATH
                else:
                    color = self.COLOR_TILE if tile.filled else self.COLOR_BG
                pygame.draw.rect(screen, color,
                                 (x, y,
                                  rect_size, rect_size))

                x += self.tile_size
            x = self.OFFSET + self.WALL_SIZE
            y += self.tile_size


if __name__ == "__main__":
    pymaze = PyMaze(generate_speed=1, solve_speed=10, size=40)
    pymaze.run()