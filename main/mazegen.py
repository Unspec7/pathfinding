import random
import astar


class Graph(object):
    def __init__(self, size):
        self.count = 0
        self.size = size
        self.all_nodes = [[None for x in range(size)] for y in range(size)]
        self.unvisited_nodes = []

        for x in range(size):
            for y in range(size):
                self.all_nodes[x][y] = Node(x, y)
                self.unvisited_nodes.append([x, y])

    def represent(self):
        count = 1
        for x in range(self.size):
            for y in range(self.size):
                if count % 101 != 0:
                    if self.all_nodes[x][y].wall is False:
                        print("O", end="")
                    elif self.all_nodes[x][y].wall is True:
                        print("X", end="")
                else:
                    if self.all_nodes[x][y].wall is False:
                        print("O")
                    elif self.all_nodes[x][y].wall is True:
                        print("X")
                count += 1


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
        self.neighbors = getneighbors(self)


def getneighbors(node):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direct in direction:
        neighbor = [node.x + direct[0], node.y + direct[1]]
        if 0 <= neighbor[0] < 101 and 0 <= neighbor[1] < 101:
            result.append(neighbor)
    return result


def generatemaze():
    firstrun = True
    while len(my_graph.unvisited_nodes) > 0:
        if firstrun:
            firstrun = False
            graph2maze()
        else:
            unvisit = my_graph.unvisited_nodes[0]
            stack.append(my_graph.all_nodes[unvisit[0]][unvisit[1]])
            graph2maze()

def graph2maze():
    while len(stack) > 0:
        my_graph.count += 1
        current = stack.pop()
        # Check neighbors to see if they're visited or not
        unvisitedneighbors = []
        for items in current.neighbors:
            neighbor = my_graph.all_nodes[items[0]][items[1]]
            if not neighbor.visited:
                unvisitedneighbors.append(neighbor)

        # If it has unvisited neighbors, add those to a list
        if len(unvisitedneighbors) != 0:
            # Put old guy back in (since he had unvisited neighbors)
            stack.append(current)

            # Set new current
            current = random.choice(unvisitedneighbors)
            current.visited = True

            # Remove from visited lists
            #my_graph.unvisited_nodes.remove([current.x, current.y])

            # Calculate wall chances
            chance = random.randint(0, 101)
            if chance <= 30:
                # Make wall
                current.wall = True
            else:
                # Push it to stack
                stack.append(current)


def getgraph():
    return my_graph


my_graph = Graph(101)
my_graph.all_nodes[0][0].wall = False
my_graph.all_nodes[0][0].visited = True
stack = [my_graph.all_nodes[0][0]]
my_graph.unvisited_nodes.remove([0, 0])
graph2maze()
my_graph.represent()
parent, cost = astar.a_star_search(my_graph, Node(0,0), Node(30,30))

for key in parent:
    print (parent[key])
for key in cost:
    print (cost[key])


