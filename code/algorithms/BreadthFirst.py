import copy
from ..classes.grid import Grid 

def breadth_first(grid):
    archive  = {}
    archive[grid] = 0
    queue = []
    queue.append(grid)

    total_moves = 0
    while queue and total_moves < 6:
        print("hi")
        grid = queue.pop(0)
        for row in grid.grid:
            #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
            print(" ".join(str(cell) for cell in row))
        print()
        if Grid.grid_solved(grid):
            solved_grid = grid
            print("Yay solved")
            print(solved_grid.grid)
            for row in solved_grid.grid:
                #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
                print(" ".join(str(cell) for cell in row))
            print()
        else:
            # print(f"current grid {grid}")
            # print()
            child_grids = Grid.get_moves(grid)
            # print(child_grids)
            for grids in child_grids:
                total_moves += 1
                new_grid = copy.deepcopy(grids)
                for row in new_grid.grid:
                    #ADD SOURCE THAT SHOWED HOW TO REMOVE  '' from letter
                    print(" ".join(str(cell) for cell in row))
                print()
                if new_grid in archive:
                    print('FOUNDD')
                    continue
                else:
                    queue.append(new_grid)
                    archive[new_grid] = 0
        print(queue)


        