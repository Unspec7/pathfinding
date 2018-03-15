from heapq import *


def heuristic(graph):
    for i in range(0, 101):
        for j in range(0, 101):
            x = graph.master[i][j].x-graph.master[100][100].x
            y = graph.master[i][j].y - graph.master[100][100].y
            graph.master[i][j].h = abs(x)+abs(y)


def computepath(graph, openlist, closedlist, count):
    s = heappop(openlist)
    s.f = s.g + s.h
    heappush(closedlist, s)
    graph.master[s.x][s.y].searchval = count
    while graph.master[100][100].g > s.f:
        for actions in s.neighbors:
            successor = graph.master[actions[0]][actions[1]]
            if successor.searchval < count:
                successor.g = 99999999999
                successor.searchval = count
            if successor.g > s.g + s.ac:
                successor.g = s.g + s.ac
                successor.parent = s
                if successor in openlist:
                    for i in range(0, len(openlist)):
                        if (openlist[i].x == successor.x) and (openlist[i].y == successor.y):
                            openlist[i] = openlist[-1]
                            openlist.pop()
                            heapify(openlist)
                            break
                successor.f = successor.g + successor.h
                heappush(openlist, successor)
        if len(openlist)>0:
            s = heappop(openlist)
            while s in closedlist:
                if len(openlist) > 0:
                    s = heappop(openlist)
            s.f = s.g + s.h
            heappush(closedlist, s)
            graph.master[s.x][s.y].searchval = count

    return graph, openlist, closedlist


def search(graph):
    heuristic(graph)
    source = graph.master[0][0]
    sink = graph.master[100][100]
    curr = source
    count = 0
    while curr.x != sink.x and curr.y != sink.y:
        count += 1
        curr.g = 0
        curr.searchval = count
        for actions in curr.neighbors:
            neighbor = graph.master[actions[0]][actions[1]]
            if neighbor.wall:
                neighbor.ac = 99999999999
        sink.g = 99999999999
        sink.searchval = count
        openlist = []
        closedlist = []
        curr.f = curr.g + curr.h
        heappush(openlist, curr)
        graph, openlist, closedlist = computepath(graph, openlist, closedlist, count)
        if len(openlist)==0:
            print("no path")
            break
        iter = sink
        path = []
        while iter.parent != curr:
            path.append(iter)
            iter = iter.parent
        while path:
            nextmove = path.pop()
            if not nextmove.wall:
                curr = nextmove
            if nextmove.wall:
                nextmove.ac = 99999999999
                break
    print("found path")
    graph.path_found = True


def a_star_search(graph):
    graph.need_clean = True
    graph.path_found = False
    source = graph.master[0][0]
    sink = graph.master[10][10]
    source.h = heuristic(source, sink)
    source.f = source.h
    openlist = []
    count = 0
    heappush(openlist, source)

    while len(openlist) > 0:
        count += 1
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
                neighbor.g = current.g + 1
                neighbor.f = neighbor.g+neighbor.h
                heappush(openlist, neighbor)

    print("Nodes expanded: " + str(count))
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph


def a_star_backwards(graph):
    graph.need_clean = True
    graph.path_found = False
    source = graph.master[100][100]
    sink = graph.master[0][0]
    source.h = heuristic(source, sink)
    source.f = source.h
    openlist = []
    count = 0
    heappush(openlist, source)

    while len(openlist) > 0:
        count += 1
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
                neighbor.f = neighbor.g + neighbor.h
                heappush(openlist, neighbor)

    print("Nodes expanded: " + str(count))
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph


def adaptive_a_star_search(graph):
    graph.need_clean = True
    graph.path_found = False
    source = graph.master[0][0]
    sink = graph.master[100][100]
    source.h = heuristic(source, sink)
    source.f = source.h
    openlist = []
    count = 0
    heappush(openlist, source)

    while len(openlist) > 0:
        count += 1
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

    print("Nodes expanded: " + str(count))
    if sink.searchvisit is not True:
        graph.path_found = False
    return graph
