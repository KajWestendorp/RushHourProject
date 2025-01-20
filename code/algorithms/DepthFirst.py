"""Pseudocode:

Create a stack
Create a dictionary of visited gameboards

Get top item from the stack

Check while solved

Get each possible move if it does not already appear

put it on the stack"""

import copy
from classes.grid import Grid 

class DepthFirst:
    """
    Depth first algorithm
    """

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.states = [""]
        self.best_solve = None
        self.archive = {}

    def get_next_state(self):
        return self.states.pop()
    
    def build_child_moves(self, grid):
        child_moves = Grid.get_moves(grid)
        self.archive[grid] = 1
        self.states.append[grid]
        while len(self.states) > 0:
            #Check for solve  
            for moves in child_moves:
                new_grid = copy.deepcopy(grid)
                new_grid = Grid(moves)
                self.states.append(new_grid)


    def run(self):
        while self.states:
            
                



                #check if the newgrid is already in the archive as a key




    def __repr__(self):
        return self.grid
