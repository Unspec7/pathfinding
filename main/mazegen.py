class Graph(object):
    def __init__(self, size):
        self.size = size
        self.all_nodes = [[None for x in range(size)] for y in range(size)]

        for x in range(size):
            for y in range(size):
                self.all_nodes[x][y] = Node(x, y)


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
        #self.neighbors = getneighbors(self)
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.wall = False
        self.visited = False
        # Parent is only used for DFS maze generation
        self.parent = None


def getneighbors(node):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direct in direction:
        neighbor = [node.x + direct[0], node.y + direct[1]]
        if 0 <= neighbor[0] < 101 and 0 <= neighbor[1] < 101:

            result.append(neighbor)
    return result


def graph2maze(graph):
    count = 1
    graph.all_nodes[0].wall = False
    graph.all_nodes[0].visited = True
    graph.all_nodes[0].parent = graph.all_nodes[0]
    my_neighbors = neighbors(graph.all_nodes[0])

    #pick random neighbor code
    while count != 10201:

        count += 1


my_graph = Graph(101)
my_graph.represent()
