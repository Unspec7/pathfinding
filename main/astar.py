from heapq import *

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.wall = False
        self.visited = False
        # A list of coordinates of it's neighbors sored in a [x, y] position
        #self.neighbors = getneighbors(self)

    def __lt__(self, other):
        '''if self.x == other.x:
            return self.y < other.y
        return self.x < other.x'''
        return self.f < other.f

def getneighbors(node):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direct in direction:
        neighbor = Node(node.x + direct[0], node.y + direct[1])
        if 0 <= neighbor.x < 101 and 0 <= neighbor.y < 101:
            result.append(neighbor)
    return result

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
    x = curr.x - goal.x
    y = curr.y - goal.y
    return abs(x) + abs(y)


def a_star_search(graph, source, sink):
    frontier = []
    #heappush(source, 0)
    heappush(frontier, source)
    parent = {}
    cost_so_far = {}
    parent[str(source)] = None
    cost_so_far[str(source)] = 0
    count = 0

    #while not frontier.empty():
    while len(frontier)>0:
        current = heappop(frontier)
        if current == sink:
            break
        print((str(source)))
        for next in getneighbors(current):
            if count == 10201:
                break
            new_cost = cost_so_far[str(current)] + heuristic(current, sink)
            current.f = new_cost
            if next not in cost_so_far or new_cost < cost_so_far[str(next)]:
                cost_so_far[str(next)] = new_cost
                priority = new_cost + heuristic(sink, next)
                next.f = priority
                #frontier.put(next, priority)
                cost_so_far[str(next)] = priority
                heappush(frontier, next)
                parent[str(next)] = current
                count += 1
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
        if not graph.neighbors(current):
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                #priority = new_cost + heuristic(source, next)
                #priority = new_cost + heuristic(sink, next)
                priority = new_cost
                frontier.put(next, priority)
                parent[next] = current

    return parent, cost_so_far
