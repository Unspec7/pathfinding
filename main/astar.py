import heapq

class AStarSeach(object):
    def __init__(self):
        self.opened = []
        self.closed = set()
        self.squares = []
        self.grid_height = 101 #Keep in mind indexes run from 0 to 100
        self.grid_width = 101
        heapq.heapify(self.opened)
