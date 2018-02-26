import random
import pickle


class Graph(object):
    def __init__(self, size):
        self.count = 0
        self.size = size
        self.path_found = False
        self.need_clean = True
        self.master = [[None for x in range(size)] for y in range(size)]
        self.unvisited = []
        ident = 0
        for x in range(size):
            for y in range(size):
                self.master[x][y] = Node(x, y, ident)
                self.unvisited.append([x, y])
                ident += 1

    def represent(self):
        count = 1
        for x in range(self.size):
            for y in range(self.size):
                if count % 101 != 0:
                    if self.master[x][y].wall is False:
                        print("O", end="")
                    elif self.master[x][y].wall is True:
                        print("X", end="")
                else:
                    if self.master[x][y].wall is False:
                        print("O")
                    elif self.master[x][y].wall is True:
                        print("X")
                count += 1

    def clean(self):
        if self.clean is False:
            for x in range(self.size):
                for y in range(self.size):
                    self.master.searchvisit = False
                    self.master.parent = []

    def diagnose(self):
        done = True
        for x in range(101):
            for y in range(10):
                if not self.master[x][y].visited:
                    done = False

        if done:
            print("All nodes have been visited")
        else:
            print("There are unvisited nodes")
        print("Ran " + str(self.count) + " times")



class Node(object):
    def __init__(self, x, y, ident):
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = self.g + self.h
        self.wall = False
        self.visited = False
        self.searchvisit = False
        self.parent = []
        # A list of coordinates of it's neighbors sored in a [x, y] position
        self.neighbors = getneighbors(self)
        self.id = ident
    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def define_self(self):
        print("Coords: (" + str(self.x) + ", " + str(self.y) + ")")
        print("Is wall?: " + str(self.wall))
        print("Visited?: " + str(self.visited))


def getneighbors(node):
    direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    result = []
    for direct in direction:
        neighbor = [node.x + direct[0], node.y + direct[1]]
        if 0 <= neighbor[0] < 101 and 0 <= neighbor[1] < 101:
            result.append(neighbor)
    return result


def generatemaze(graph):
    """Generate a maze using DFS"""
    count = 0
    stack = []
    while len(graph.unvisited) > 0:
        """While there are still unvisited nodes, keep going"""
        graph2maze(stack, graph)
        count += 1

    graph.count = count
    entrance_exit_generation(graph)


def entrance_exit_generation(graph):
    """
    Generate entrance and exit by making sure (0,0) and (100,100) aren't
    walls along with the two surround blocks
    """
    graph.master[0][0].wall = False
    graph.master[1][0].wall = False
    graph.master[0][1].wall = False
    graph.master[1][1].wall = False
    graph.master[100][100].wall = False
    graph.master[100][99].wall = False
    graph.master[99][100].wall = False
    graph.master[99][99].wall = False


def graph2maze(stack, graph):
    # Pick a random index
    index = random.randint(0, len(graph.unvisited)-1)

    # Use index to find coordinate tuple
    coords = graph.unvisited[index]

    # Use coordinate to set selected node
    current = graph.master[coords[0]][coords[1]]
    current.visited = True
    current.wall = False

    # Push to stack
    stack.append(current)

    # Remove from unvisited list using previously found index
    graph.unvisited.pop(index)

    while len(stack) > 0:
        current = stack.pop()
        # Check neighbors to see if they're visited or not
        valid_neighbors = []
        for items in current.neighbors:
            neighbor = graph.master[items[0]][items[1]]
            if not neighbor.visited:
                valid_neighbors.append(neighbor)

        # If it has unvisited neighbors, add those to a list
        if len(valid_neighbors) != 0:
            # Put old guy back in (since he had unvisited neighbors)
            stack.append(current)

            # Set new current
            current = random.choice(valid_neighbors)
            current.visited = True

            # Remove from unvisited
            graph.unvisited.remove([current.x, current.y])

            # Calculate wall chances
            chance = random.randint(0, 100)
            if chance <= 25:
                # Make wall and don't push it back
                current.wall = True
            else:
                # It's a corridor, so push it to stack
                stack.append(current)


"""
def DFSMaze(graph):
    DFSstack = []
    reference = Graph(100)
    curr = random.choice(random.choice(graph.all_nodes))
    DFSstack.append(curr)
    chance = 100
    while len(DFSstack) != 0:
        my_graph.count += 1
        curr.visited = True
        unvisited = []
        for NB in curr.neighbors:
            neighbor = graph.all_nodes[NB[0]][NB[1]]
            if not neighbor.visited:
                unvisited.append(neighbor)

        if len(unvisited) == 0:
            curr = DFSstack.pop()
            chance = random.randint(0, 101)
            continue
        if chance <= 30:
            curr.wall = True
            curr = DFSstack.pop()
            chance = random.randint(0, 101)
            continue
        chance = random.randint(0, 100)
        curr = random.choice(unvisited)
        DFSstack.append(curr)
"""

"""
my_graph = Graph(101)
generatemaze(my_graph)
my_graph.represent()
my_graph.diagnose()
"""





"""
mazes = []
mazes.append(my_graph)
    #print("Graph "+str(i)+" done")
pickle_out = open("mazes.dat","wb")
pickle.dump(mazes, pickle_out)
pickle_out.close()
"""



