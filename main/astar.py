from heapq import *

class Square(object):
    def __init__(self, x, y, valid):
        self.x = x
        self.y = y
        self.valid = valid
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0
        self.visited = False


def heuristic(curr, goal):
    (x1, y1) = curr
    (x2, y2) = goal
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(graph, source, sink):
    frontier = []
    heappush(source, 0)
    parent = {}
    cost_so_far = {}
    parent[source] = None
    cost_so_far[source] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == sink:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(sink, next)
                frontier.put(next, priority)
                parent[next] = current

    return parent, cost_so_far

def a_star_backwards(graph, source, sink):
    frontier = []
    heappush(sink, 0)
    parent = {}
    cost_so_far = {}
    parent[sink] = None
    cost_so_far[sink] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == source:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(source, next)
                priority = new_cost + heuristic(sink, next)
                frontier.put(next, priority)
                parent[next] = current

    return parent, cost_so_far
