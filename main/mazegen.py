class Graph(object):
    def __init__(self, size):
        self.size = size
        self.all_nodes = []
        for x in range(self.size):
            for y in range(self.size):
                self.all_nodes.append(Node(x, y))

    def represent(self):
        count = 1
        for node in self.all_nodes:
            if count % 101 != 0:
                if node.wall is False:
                    print("O", end="")
                elif node.wall is True:
                    print("X", end="")
            else:
                if node.wall is False:
                    print("O")
                elif node.wall is True:
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


def graph2maze(graph):
    graph.all_nodes[0].wall = False
    graph.all_nodes[0].visited = True


def neighbors(node):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direct in direction:
        neighbor = [node[0] + direct[0], node[1] + direct[1]]
        if 0 <= neighbor[0] < 20 and 0 <= neighbor[1] < 10:
            result.append(neighbor)
    return result

my_graph = Graph(101)
my_graph.represent()
