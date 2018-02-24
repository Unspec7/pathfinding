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
            if node is not None:
                if count % 101 != 0:
                    print("X", end = "")
                else:
                    print("X")
            else:
                print("O")
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


my_graph = Graph(101)
my_graph.represent()