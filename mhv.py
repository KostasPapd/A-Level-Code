from algoritm import *
g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS # long list, [(21, 0), (21, 2), ...]
draw_grid(g)


def breadth_first_search(graph: Graph, start: Location):
    frontier = Queue()
    frontier.put(start)
    came_from: dict[Location, Optional[Location]] = {}
    came_from[start] = None

    while not frontier.empty():
        current: Location = frontier.get()
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current

    return came_from


g = SquareGrid(30, 15)
g.walls = DIAGRAM1_WALLS

start = (8, 7)
parents = breadth_first_search(g, start)
draw_grid(g, point_to=parents, start=start)