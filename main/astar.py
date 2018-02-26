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
    heappush(openlist, source)
    while len(openlist) > 0:
        current = heappop(openlist)
        current.searchvisit = True
        if current == sink:
            graph.path_found = True
            break
        for items in current.neighbors:
            neighbor = graph.master[items[0]][items[1]]
            if neighbor.wall:
                continue

            '''don't need to check to see if openlist has shorter g value because g is always 1'''

            if not neighbor.searchvisit and neighbor not in openlist:
                neighbor.parent = current
                neighbor.h = heuristic(neighbor, sink)
                neighbor.g = current.g+1
                neighbor.f = neighbor.g+neighbor.h
                heappush(openlist, neighbor)
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
    heappush(openlist, source)
    while len(openlist) > 0:
        current = heappop(openlist)
        current.searchvisit = True
        if current == sink:
            graph.path_found = True
            break
        for items in current.neighbors:
            neighbor = graph.master[items[0]][items[1]]
            if neighbor.wall:
                continue
            if not neighbor.searchvisit and neighbor not in openlist:
                neighbor.parent = current
                neighbor.h = heuristic(neighbor, sink)
                neighbor.g = current.g+1
                neighbor.f = neighbor.g+neighbor.h
                heappush(openlist, neighbor)
                heappush(openlist, neighbor)
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph

def adaptive_a_star_search(graph):
    graph.clean = False
    source = graph.master[0][0]
    sink = graph.master[100][100]
    source.h = heuristic(source, sink)
    source.f = source.h
    openlist = []
    heappush(openlist, source)
    while len(openlist) > 0:
        current = heappop(openlist)
        current.searchvisit = True
        if current == sink:
            graph.path_found = True
            break
        for items in current.neighbors:
            neighbor = graph.master[items[0]][items[1]]
            if neighbor.wall:
                continue

            '''don't need to check to see if openlist has shorter g value because g is always 1'''

            if not neighbor.searchvisit and neighbor not in openlist:
                neighbor.parent = current
                neighbor.h = heuristic(neighbor, sink)
                neighbor.g = current.g+1
                neighbor.f = neighbor.g+neighbor.h
                heappush(openlist, neighbor)
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph