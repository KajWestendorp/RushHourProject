import copy
from ..classes.grid import Grid 

def breadth_first(grid):
    archive  = {}
    archive[grid] = 0
    queue = []
    queue.append(grid)

    total_moves = 0
    while queue:
        grid = queue.pop()
        total_moves += 1
        if Grid.grid_solved(grid):
            solved_grid = grid
            print("Yay solved")
            print(solved_grid.grid)
            for row in solved_grid.grid:
                #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
                print(" ".join(str(cell) for cell in row))
            print()
        else:
            child_grids = Grid.get_moves(grid)
            for grids in child_grids:
                new_grid = copy.deepcopy(grids)
                if new_grid in archive:
                    continue
                else:
                    queue.append(grids)
                    archive[grids] = 0