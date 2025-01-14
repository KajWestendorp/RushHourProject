import os
import pandas as pd
from cars import *

class Grid():
    def __init__(self, boardsize):

        #col and row
        self.boardsize = boardsize

    def create_grid(self):
        self.grid = []

        for _ in range(self.boardsize + 2):
            row = []
            for _ in range(self.boardsize + 2):
                row.append(0)
            self.grid.append(row)

        return self.grid


    def add_borders(self):
        for _ in range(self.boardsize + 2):
            self.grid[0][_] = 1
            self.grid[self.boardsize + 1][_] = 1
            self.grid[_][0] = 1
            self.grid[_][self.boardsize + 1] = 1

        return self.grid
    
    def update_board(self):

    

test = Grid(6)
print(Grid.create_grid(test))
print(Grid.add_borders(test))


script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_test.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

print(boardposition1)

print(Grid.add_cars(test, boardposition1))
