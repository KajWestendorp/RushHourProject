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
        



        return self.grid
    
    def add_cars_to_board(self, cars):

        coords = {}
        for _, car in cars.iterrows():
        # Checks the orientation of the car and adjusts the column by 1 to include the space above it and row plus 1 for vertical cars
        # TODO: WIll need to add a check for car length later on to ensure the corret amount is being added to the coords for trucks
            if car['orientation'] == 'V':
                coords[car['car']] = ((car['col'], car['row']), (car['col'] + 1, car['row']))
            else:
                coords[car['car']] = ((car['col'], car['row']), (car['col'], car['row'] + 1))

        for car in coords:
            coordinates = coords[car]
            for row, col in coordinates:
                self.grid[row][col] = (car)

        print(self.cars)
        return self.grid

    

test = Grid(6)
print(Grid.create_grid(test))
print(Grid.add_borders(test))


Cars(boardposition1)
cardf = Cars.add_cars(test)
print(Grid.add_cars_to_board(test, cardf))


script_dir = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join("..", "gameboards", "Rushhour6x6_test.csv")

# Construct the path to the gameboard file
board_file = os.path.normpath(os.path.join(script_dir, relative_path))

boardposition1 = pd.read_csv(board_file, sep=',', encoding='utf-8')

print(boardposition1)
