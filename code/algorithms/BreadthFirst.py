import copy
from ..classes.grid import Grid 

def breadth_first(grid):
    archive  = {}
    archive[grid] = 0
    queue = []
    queue.append(grid)

    total_moves = 0
    while queue:
        grid = queue.pop(0)
        total_moves += 1
        if Grid.grid_solved(grid):
            solved_grid = grid
            print("Yay solved")
            for row in solved_grid.grid:
                #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
                print(" ".join(str(cell) for cell in row))
            print()
            return print(total_moves)
        else:
            child_grids = Grid.get_moves(grid)
            for grids in child_grids:
                new_grid = copy.deepcopy(grids)
                if Grid.grid_solved(new_grid):
                    solved_grid = new_grid
                    print("Yay solved")
                    for row in solved_grid.grid:
                        #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
                        print(" ".join(str(cell) for cell in row))
                    print()
                    return print(total_moves)
                queue.append(new_grid)
                if new_grid in archive:
                    continue
                else:
                    archive[new_grid] = new_grid.grid
    print(queue)
    for row in new_grid.grid:
        #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
        print(" ".join(str(cell) for cell in row))
    print()


        