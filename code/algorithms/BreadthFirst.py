
from ..classes.grid import Grid 

# https://stackoverflow.com/questions/79037234/reduce-memory-use-for-breadth-first-search
# used to find deque and to turn archive into a set
from collections import deque

def breadth_first(grid):
    archive = set()
    archive.add(grid)
    queue = deque([grid])

    total_moves = 0
    while queue:
        grid = queue.popleft()
        total_moves += 1

        # print(f"Processing grid (Move {total_moves}):")
        # for row in grid.grid:
        #     print(" ".join(str(cell) for cell in row))
        # print()

        if Grid.grid_solved(grid):
            print("Solution found!")
            for row in grid.grid:
                print(" ".join(str(cell) for cell in row))
            print()
            return print("Total moves:", total_moves)

        child_grids = Grid.get_moves(grid)
        # print(f"Generated {len(child_grids)} child grids")
        for child_grid in child_grids:
            if child_grid in archive:
                # print("Skipping visited grid:")
                # for row in child_grid.grid:
                #     print(" ".join(str(cell) for cell in row))
                # print()
                continue

            if Grid.grid_solved(child_grid):
                print("Solution found!")
                for row in child_grid.grid:
                    print(" ".join(str(cell) for cell in row))
                print()
                return print("Total moves:", total_moves)

            # print("Adding child grid to queue:")
            # for row in child_grid.grid:
            #     print(" ".join(str(cell) for cell in row))
            # print()
            queue.append(child_grid)
            archive.add(child_grid)

    print("No solution found")
    return



        