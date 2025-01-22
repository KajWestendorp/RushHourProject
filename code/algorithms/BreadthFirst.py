from ..classes.grid import Grid
from collections import deque
import pandas as pd

def breadth_first(grid):
    """ 
        Implementation of bfs for rush hour problem
        TODO: ADD MORE DETAILED DOC STRING
    """

    # Archive as a set to store grids
    archive = set()
    archive.add(grid)
    # the queue is made up of a tuple, the grid and the depth of the tree layers to count moves correctly 
    # (https://stackoverflow.com/questions/52513309/tracking-depth-in-a-breadth-first-search-of-a-directed-tree)
    queue = deque([(grid, 0)])  

    #The parent dict for each grid starting at None with the beginning
    parent_of_grid = {}  
    parent_of_grid[grid] = None

    # When the queue is not empty
    while queue:

        #first grid and first depth taken from the queue
        grid, depth = queue.popleft()

        #Check if solution has been found
        if Grid.grid_solved(grid):
            print("Solution found!")
            
            # Prints the number of moves a.k.a the depth that it took to reach the solution
            print(f"Moves until solution: {depth}")

            # Call backtrace function to show the shortest path
            path = backtrace_path(grid, parent_of_grid)

            #Start printing
            print()
            for move, grid in enumerate(path):
                if move == 0:
                    print("Start position")
                else:
                    print(f"Move number {move}:")
                for row in grid.grid:
                    print(" ".join(str(cell) for cell in row))
            print()
            return grid, get_output(grid, parent_of_grid)

        #Call get_moves function to get the child grid nodes from the current Node
        child_grids = Grid.get_moves(grid)
        for child_grid in child_grids:

            #If this grid config has already been handeled we skip addding it to the queu, archive and parent dict
            if child_grid in archive:
                continue
            
            # Add the parent to the child_grid in the dict
            parent_of_grid[child_grid] = grid 

            # Lower the depth and add child to dlist
            queue.append((child_grid, depth + 1))

            #Avoid going to two grid positions so we archive it
            archive.add(child_grid)

    print("No solution found womp womp")
    return

def backtrace_path(grid, parents):
    """
    Backtrace's tehe path that led to the quickest solution from BFS
    """
    shortest_path = []
    
    # If we reach None its the start
    while grid is not None:

        # Append current grid to shortest path list of grids
        shortest_path.append(grid)



        # Get the next parent
        grid = parents[grid]
    
    #Reverse it, because we have to search from solution to start but we want to print from start to solution
    shortest_path.reverse()

    return shortest_path

def get_output(grid, parents):
    """
    """
    
    output_list = []
    
    while grid is not None:

        #Get next parent of the new parent XD confujsing
        parent = parents[grid]  

        if parent is None: 
            break

        # Compare the parent grid to the current grid to find the car that moved, using zip to loop through both lists of cars at the same time
        for car, parent_car in zip(grid.cars, parent.cars):

            #Check orientation and whether this car even moved
            if car.orientation == 'H' and car.col != parent_car.col:

                # Check steps the car moved
                output_list.append((car.name, car.col - parent_car.col))
                break
            elif car.orientation == 'V' and car.row != parent_car.row:

                # Check how many steps the car moved 
                output_list.append((car.name, car.row - parent_car.col))
                break

        # Move onto next parent
        grid = parent

    # Reverse the output list to show the moves in the correct order (start to solution)
    output_list.reverse()

    df_output = pd.DataFrame(output_list, columns = ['car', 'move'])
    return df_output
