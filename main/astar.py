from heapq import *


def heuristic(curr, goal):
    x = curr.x - goal.x
    y = curr.y - goal.y
    return abs(x) + abs(y)


def a_star_search(graph):
    source = graph.master[0][0]
    sink = graph.master[100][100]
    source.h = heuristic(source,sink)
    source.f = source.h
    openlist = []
    closedlist = []
    #heappush(source, 0)
    heappush(openlist,source)

    parent = {}
    cost_so_far = {}
    parent[source.id] = None
    cost_so_far[source.id] = 0
    count = 0

    #while not frontier.empty():
    while len(openlist)>0:
        sorted(openlist, key=lambda node: node.f, reverse=True)
        current = heappop(openlist)
        closedlist.append(current)
        current.searchvisit = True
        if current == sink:
            break
        for items in current.neighbors:
            neighbor = graph.master[items[0]][items[1]]
            if neighbor.wall:
                continue
            if neighbor not in closedlist and neighbor not in openlist:
                neighbor.parent = current
                neighbor.h = heuristic(neighbor, sink)
                neighbor.g = current.g+1
                neighbor.f = neighbor.g+neighbor.h
                heappush(openlist, neighbor)
                heappush(openlist, neighbor)
    return graph

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
