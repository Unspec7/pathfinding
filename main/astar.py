import heapq


class Square(object):
    def __init__(self, x, y, valid):
        """""
        A square for the agent to be on
        @:param x square's x coordinate
        @:param y square's y coordinate
        @:param is the cell a valid cell, aka reachable and not a wall
        """
        self.x = x
        self.y = y
        self.valid = valid
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.visited = False


class AStarSeach(object):
    def __init__(self):
        self.opened = []
        self.closed = set()
        self.squares = []
        self.grid_height = 101 #Keep in mind indexes run from 0 to 100
        self.grid_width = 101
        heapq.heapify(self.opened)

