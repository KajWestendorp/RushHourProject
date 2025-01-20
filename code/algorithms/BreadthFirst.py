

def breadth_first(grid):
    archive  = {}
    archive[grid] = 0
    queue = []

    queue.append(grid)
    depth = 3
    while queue:
        grid = queue.pop()

        if len(grid) < depth:
            

