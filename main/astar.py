from heapq import *


def heuristic(curr, goal):
    x = curr.x - goal.x
    y = curr.y - goal.y
    return abs(x) + abs(y)


def a_star_search(graph):
    graph.clean = False
    source = graph.master[0][0]
    sink = graph.master[100][100]
    source.h = heuristic(source, sink)
    source.f = source.h
    openlist = []
    closedlist = []
    # heappush(source, 0)
    heappush(openlist, source)

    parent = {}
    cost_so_far = {}
    parent[source.id] = None
    cost_so_far[source.id] = 0
    count = 0

    # While not frontier.empty():
    while len(openlist) > 0:
        count += 1
        sorted(openlist, key=lambda node: node.f, reverse=True)
        current = heappop(openlist)
        closedlist.append(current)
        current.searchvisit = True
        if current == sink:
            graph.path_found = True
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
    print("Nodes expanded: " + str(count))
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph


def a_star_backwards(graph):
    graph.clean = False
    source = graph.master[100][100]
    sink = graph.master[0][0]
    source.h = heuristic(source, sink)
    source.f = source.h
    openlist = []
    closedlist = []
    # heappush(source, 0)
    heappush(openlist, source)

    parent = {}
    cost_so_far = {}
    parent[source.id] = None
    cost_so_far[source.id] = 0
    count = 0

    # While not frontier.empty():
    while len(openlist) > 0:
        count += 1
        sorted(openlist, key=lambda node: node.f, reverse=True)
        current = heappop(openlist)
        closedlist.append(current)
        current.searchvisit = True
        if current == sink:
            graph.path_found = True
            break
        for items in current.neighbors:
            neighbor = graph.master[items[0]][items[1]]
            if neighbor.wall:
                continue
            if neighbor not in closedlist and neighbor not in openlist:
                neighbor.parent = current
                neighbor.h = heuristic(neighbor, sink)
                neighbor.g = current.g + 1
                neighbor.f = neighbor.g + neighbor.h
                heappush(openlist, neighbor)
                heappush(openlist, neighbor)
    print("Nodes expanded: " + str(count))
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph
